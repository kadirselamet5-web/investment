"""Internet Archive'dan 1923–1950 Türkçe süreli yayın ve kitapların OCR metinlerini (_djvu.txt) toplar.

Kullanım: python3 ia_topla.py <çıktı_klasörü>
- <çıktı>/ia_kayitlar.tsv : kimlik, tarih, başlık, koleksiyon, metin dosyası, boyut
- <çıktı>/text/<kimlik>.txt
Sorgular aşağıdaki SORGULAR listesinde; sonuçlar birleştirilir.
"""
import os, sys, time, concurrent.futures as cf
import requests

OUT = sys.argv[1]
S = requests.Session()
S.headers["User-Agent"] = "academic research (sigir-arastirmasi)"
TARIH = "date:[1923-01-01 TO 1950-12-31]"
SORGULAR = [
    f"(language:tur OR language:turkish OR language:ottoman OR language:\"Turkish\") AND mediatype:texts AND {TARIH}",
    "collection:halk-bilgisi-haberleri",
    "collection:ulku-halkevi-dergisi",
    "identifier:he-* AND mediatype:texts",
    "identifier:d_ulku* AND mediatype:texts",
    "askeri-tibbi-baytari-mecmuasi",
]
for k in ["ziraat", "zirai", "hayvan", "hayvancılık", "baytar", "baytari", "veteriner", "sığır", "sığırcılık", "köy", "köylü",
          "çiftçi", "halkevi", "zootekni", "yem", "süt", "mera", "tarım", "iktisat", "iktisadi", "kalkınma", "mecmuası",
          "dergisi", "gazetesi", "resmi gazete", "ziraat vekaleti", "yüksek ziraat", "hıfzıssıhha", "köy kanunu"]:
    SORGULAR.append(f"title:({k}) AND mediatype:texts AND {TARIH}")


def ara(q):
    out, sayfa = [], 1
    while True:
        r = S.get("https://archive.org/advancedsearch.php", params={
            "q": q, "fl[]": ["identifier", "title", "date", "collection", "language"], "rows": 500, "page": sayfa,
            "output": "json"}, timeout=120).json()["response"]
        out += r["docs"]
        if sayfa * 500 >= r["numFound"]:
            return out
        sayfa += 1


def metin_indir(doc):
    kid = doc["identifier"]
    hedef = os.path.join(OUT, "text", kid + ".txt")
    if os.path.exists(hedef):
        return kid, os.path.getsize(hedef), "var"
    for i in range(4):
        try:
            files = S.get(f"https://archive.org/metadata/{kid}/files", timeout=120).json().get("result", [])
            txts = [f["name"] for f in files if f["name"].endswith("_djvu.txt")]
            if not txts:
                return kid, 0, "OCR yok"
            parca = []
            for t in txts:
                r = S.get(f"https://archive.org/download/{kid}/{t}", timeout=600)
                parca.append(f"##### {t}\n" + r.text)
            open(hedef, "w", encoding="utf-8").write("\f".join(parca))
            return kid, os.path.getsize(hedef), f"{len(txts)} dosya"
        except (requests.RequestException, ValueError):
            time.sleep(2 ** (i + 1))
    return kid, 0, "HATA"


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "text"), exist_ok=True)
    docs = {}
    for q in SORGULAR:
        for d in ara(q):
            docs.setdefault(d["identifier"], d)
        print(len(docs), q, flush=True)
    with cf.ThreadPoolExecutor(8) as ex, open(os.path.join(OUT, "ia_kayitlar.tsv"), "w") as f:
        f.write("kimlik\ttarih\tbaslik\tkoleksiyon\tmetin_bayt\tdurum\n")
        liste = list(docs.values())
        for d, (kid, boyut, durum) in zip(liste, ex.map(metin_indir, liste)):
            kol = d.get("collection", "")
            kol = ";".join(kol) if isinstance(kol, list) else kol
            f.write(f"{kid}\t{d.get('date', '')[:10]}\t{str(d.get('title', '')).replace(chr(9), ' ')}\t{kol}\t{boyut}\t{durum}\n")
            f.flush()
