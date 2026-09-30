"""TBMM Açık Erişim'de OCR metni olmayan kayıtları indirip tesseract (tur) ile metne çevirir.

Kullanım: python3 tbmm_ocr.py <items.json> <çıktı_klasörü> <handle> [<handle> ...]
Her PDF için <çıktı>/<handle_>/<pdf_adı>.txt yazılır (sayfa ayırıcı \\f); PDF işlendikten sonra silinir.
Sayfalar 250 dpi gri tonlamada işlenir; 4 tesseract süreci paralel çalışır (OMP_THREAD_LIMIT=1).
"""
import json, os, subprocess, sys, tempfile, concurrent.futures as cf
import requests, pymupdf

API = "https://acikerisim.tbmm.gov.tr/server/api"
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 (academic research)"
ENV = dict(os.environ, OMP_THREAD_LIMIT="1")


def sayfa_ocr(png):
    r = subprocess.run(["tesseract", png, "-", "-l", "tur", "--psm", "3"], capture_output=True, text=True, env=ENV)
    os.remove(png)
    return r.stdout


def hazirla(is_):
    """PDF'i indirir ve sayfaları PNG'ye çizer (OCR işçileriyle eşzamanlı çalışır)."""
    hedef, url, etiket = is_
    gecici = tempfile.mkdtemp(prefix="tbmm_")
    pdf = os.path.join(gecici, "x.pdf")
    with S.get(url, stream=True, timeout=1800) as r, open(pdf, "wb") as f:
        for parca in r.iter_content(1 << 20):
            f.write(parca)
    doc = pymupdf.open(pdf)
    pngler = []
    for i, p in enumerate(doc):
        png = os.path.join(gecici, f"p{i:05d}.png")
        p.get_pixmap(dpi=250, colorspace=pymupdf.csGRAY).save(png)
        pngler.append(png)
    doc.close()
    os.remove(pdf)
    return is_, gecici, pngler


def main():
    """Boru hattı: sonraki PDF arka planda indirilip çizilirken OCR işçileri iki PDF'in
    sayfalarını birlikte işler; CPU indirme ve PDF sonu beklemelerinde boşta kalmaz."""
    import shutil
    from collections import deque
    items = {it["handle"]: it for it in json.load(open(sys.argv[1]))}
    out = sys.argv[2]
    isler = []
    for h in sys.argv[3:]:
        it = items[h]
        klasor = os.path.join(out, h.replace("/", "_"))
        os.makedirs(klasor, exist_ok=True)
        try:
            bundles = S.get(f"{API}/core/items/{it['uuid']}/bundles", timeout=120).json()["_embedded"]["bundles"]
            for bu in bundles:
                if bu["name"] != "ORIGINAL":
                    continue
                bs = S.get(bu["_links"]["bitstreams"]["href"] + "?size=1000", timeout=120).json()["_embedded"]["bitstreams"]
                for b in bs:
                    hedef = os.path.join(klasor, b["name"] + ".txt")
                    if not os.path.exists(hedef):
                        isler.append((hedef, b["_links"]["content"]["href"], f"{h} {it['name'][:40]} {b['name']}"))
        except Exception as e:  # noqa: BLE001
            print(h, "LİSTE HATASI", e, flush=True)
    kalan = iter(isler)
    with cf.ThreadPoolExecutor(4) as havuz, cf.ThreadPoolExecutor(2) as hazirlik:
        hazir, aktif = deque(), deque()

        def ileri():
            is_ = next(kalan, None)
            if is_:
                hazir.append(hazirlik.submit(hazirla, is_))

        ileri(), ileri()
        while hazir or aktif:
            if hazir and len(aktif) < 2:
                f = hazir.popleft()
                ileri()
                try:
                    is_, gecici, pngler = f.result()
                except Exception as e:  # noqa: BLE001  (sonraki koşuda yeniden denenir)
                    print("HATA", e, flush=True)
                    continue
                aktif.append((is_, gecici, [havuz.submit(sayfa_ocr, p) for p in pngler]))
                continue
            (hedef, _, etiket), gecici, futs = aktif.popleft()
            metinler = [f.result() for f in futs]
            open(hedef, "w", encoding="utf-8").write("\f".join(metinler))
            shutil.rmtree(gecici, ignore_errors=True)
            print(etiket, len(metinler), "sayfa", flush=True)


if __name__ == "__main__":
    main()
