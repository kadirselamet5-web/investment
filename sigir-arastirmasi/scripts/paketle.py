"""Siteyi gönderilebilir zip parçalarına böler (her parça < SINIR).

Bütün parçalar aynı klasöre açılınca site/ yapısı (index.html + metin/) eksiksiz oluşur.
Kullanım: python3 scripts/paketle.py   → site_paket_1.zip, site_paket_2.zip, …
"""
import glob
import os
import zipfile

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(KOK, "site")
SINIR = 25 * 1024 * 1024

for eski in glob.glob(os.path.join(KOK, "site_paket*.zip")):
    os.remove(eski)

dosyalar = ["index.html"] + sorted(os.path.relpath(p, SITE) for p in glob.glob(os.path.join(SITE, "metin", "*.js")))
parca, boyut, zf = 0, 0, None
for d in dosyalar:
    yol = os.path.join(SITE, d)
    tahmin = os.path.getsize(yol) * 0.45  # sıkıştırılmış boyut için kaba tahmin
    if zf is None or boyut + tahmin > SINIR:
        if zf:
            zf.close()
        parca += 1
        zf = zipfile.ZipFile(os.path.join(KOK, f"site_paket_{parca}.zip"), "w", zipfile.ZIP_DEFLATED, compresslevel=9)
        boyut = 0
    zf.write(yol, d)
    boyut += tahmin
zf.close()
for p in sorted(glob.glob(os.path.join(KOK, "site_paket_*.zip"))):
    print(os.path.basename(p), round(os.path.getsize(p) / 2**20, 1), "MB")
