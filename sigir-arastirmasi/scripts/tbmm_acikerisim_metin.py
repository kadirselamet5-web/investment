"""TBMM Kütüphanesi Açık Erişim (DSpace 7) kayıtlarının metadatasını ve OCR metinlerini indirir.

Kullanım: python3 tbmm_acikerisim_metin.py <çıktı_klasörü> [başlangıç_yılı] [bitiş_yılı]
- <çıktı>/items.json            : bütün kayıtların metadatası
- <çıktı>/text/<handle>/<ad>.txt : dönem kayıtlarının TEXT paketindeki OCR metinleri
- <çıktı>/envanter.tsv          : kayıt başına dosya sayısı, PDF boyutu, metin boyutu
"""
import json, os, re, sys, concurrent.futures as cf
import requests

OUT = sys.argv[1]
Y1 = int(sys.argv[2]) if len(sys.argv) > 2 else 1923
Y2 = int(sys.argv[3]) if len(sys.argv) > 3 else 1950
API = "https://acikerisim.tbmm.gov.tr/server/api"
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 (academic research)"


def yil(it):
    for k in ("dc.date.issued", "dc.date", "dc.date.created"):
        for v in it["md"].get(k, []):
            m = re.search(r"\b(1[89]\d\d|20\d\d)\b", v)
            if m:
                return int(m.group(1))
            m = re.search(r"\b(13[0-9]\d)\b", v)  # rumi/hicri yıl, yaklaşık
            if m:
                return int(m.group(1)) + 584
    return None


def kayitlar():
    p = os.path.join(OUT, "items.json")
    if os.path.exists(p):
        return json.load(open(p))
    items, page = [], 0
    while True:
        r = S.get(f"{API}/discover/search/objects", params={"query": "*", "dsoType": "ITEM", "size": 100, "page": page}, timeout=120).json()
        sr = r["_embedded"]["searchResult"]
        for o in sr["_embedded"]["objects"]:
            it = o["_embedded"]["indexableObject"]
            items.append({"uuid": it["uuid"], "handle": it.get("handle"), "name": it["name"],
                          "md": {k: [v["value"] for v in vs] for k, vs in it["metadata"].items()}})
        page += 1
        if page >= sr["page"]["totalPages"]:
            break
    json.dump(items, open(p, "w"), ensure_ascii=False)
    return items


def isle(it):
    klasor = os.path.join(OUT, "text", it["handle"].replace("/", "_"))
    os.makedirs(klasor, exist_ok=True)
    bundles = S.get(f"{API}/core/items/{it['uuid']}/bundles", timeout=120).json()["_embedded"]["bundles"]
    pdf_n = pdf_mb = txt_mb = 0
    for bu in bundles:
        bs = S.get(bu["_links"]["bitstreams"]["href"] + "?size=1000", timeout=120).json()["_embedded"]["bitstreams"]
        if bu["name"] == "ORIGINAL":
            pdf_n, pdf_mb = len(bs), sum(b["sizeBytes"] for b in bs) / 1e6
        if bu["name"] == "TEXT":
            for b in bs:
                txt_mb += b["sizeBytes"] / 1e6
                hedef = os.path.join(klasor, b["name"])
                if os.path.exists(hedef) or b["sizeBytes"] == 0:
                    continue
                r = S.get(b["_links"]["content"]["href"], timeout=300)
                open(hedef, "wb").write(r.content)
    return [it["handle"], str(yil(it)), it["name"].replace("\t", " "), ";".join(it["md"].get("dc.subject", [])), str(pdf_n), f"{pdf_mb:.1f}", f"{txt_mb:.2f}"]



def _guvenli(it):
    try:
        return isle(it)
    except Exception as e:  # noqa: BLE001
        return [it["handle"], "", it["name"], "", "", "", f"HATA {e}"]


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    items = [it for it in kayitlar() if (y := yil(it)) and Y1 <= y <= Y2]
    print(len(items), "kayıt", flush=True)
    with cf.ThreadPoolExecutor(4) as ex, open(os.path.join(OUT, "envanter.tsv"), "w") as f:
        f.write("handle\tyil\tbaslik\tkonu\tpdf_sayisi\tpdf_mb\tmetin_mb\n")
        for row in ex.map(_guvenli, items):
            f.write("\t".join(row) + "\n")
            f.flush()
