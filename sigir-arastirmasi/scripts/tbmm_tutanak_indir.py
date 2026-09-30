"""TBMM Zabıt Ceridesi / Tutanak Dergisi PDF'lerini (1923–1950) indirir ve metne çevirir.

Kullanım: python3 tbmm_tutanak_indir.py <çıktı_klasörü>
Her birleşim PDF'i için <çıktı>/text/<dosya>.txt yazılır (sayfa ayırıcı: \f).
Liste <çıktı>/pdf_listesi.tsv dosyasına kaydedilir.
"""
import os, re, sys, time, concurrent.futures as cf
import requests, pymupdf

OUT = sys.argv[1]
BASE = "https://www5.tbmm.gov.tr/develop/owa/"
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 (academic research crawler)"
DONEMLER = ["d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09"]


def get(url, tries=4):
    for i in range(tries):
        try:
            r = S.get(url, timeout=120)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
        time.sleep(2 ** (i + 1))
    raise RuntimeError(url)


def pdf_listesi():
    rows = []
    for d in DONEMLER:
        n = int(d[1:])
        yy = get(f"{BASE}tutanak_dergisi_pdfler.yasama_yillari?v_meclis=1&v_donem={n}").text
        for link in re.findall(r'HREF="(tutanak_dergisi_pdfler\.birlesimler\?[^"]+)"', yy, re.I):
            link = link.replace("&amp;", "&")
            yil = re.search(r"v_yasama_yili=(\d+)", link).group(1)
            if d == "d09" and yil != "1":
                continue
            page = get(BASE + link).text
            for pdf in re.findall(r'HREF="(https?://www5\.tbmm\.gov\.tr/tutanaklar/[^"]+\.pdf)"', page, re.I):
                rows.append((d, yil, pdf.replace("http://", "https://")))
    return rows


def isle(row):
    d, yil, url = row
    ad = url.rsplit("/", 1)[1][:-4]
    txt = os.path.join(OUT, "text", ad + ".txt")
    if os.path.exists(txt):
        return ad, "var"
    if ad.startswith("eht"):  # eski harfli asıl tutanak: metin katmanı yok, Latin çevriyazısı ayrıca indiriliyor
        return ad, "atlandı (eski harf)"
    r = get(url)
    doc = pymupdf.open(stream=r.content, filetype="pdf")
    metin = "\f".join(p.get_text() for p in doc)
    with open(txt, "w", encoding="utf-8") as f:
        f.write(metin)
    return ad, len(metin)


def _safe(r):
    try:
        return isle(r)
    except Exception as e:  # noqa: BLE001
        return r[2], f"HATA {e}"


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "text"), exist_ok=True)
    liste = os.path.join(OUT, "pdf_listesi.tsv")
    if not os.path.exists(liste):
        rows = pdf_listesi()
        with open(liste, "w") as f:
            for r in rows:
                f.write("\t".join(r) + "\n")
    rows = [l.rstrip("\n").split("\t") for l in open(liste)]
    print(len(rows), "PDF", flush=True)
    with cf.ThreadPoolExecutor(12) as ex:
        for i, res in enumerate(ex.map(_safe, rows)):
            if i % 100 == 0:
                print(i, res, flush=True)
