"""Milletler Cemiyeti Antlaşmalar Dizisi (LNTS) ciltlerini treaties.un.org'dan indirip metne çevirir.

Kullanım: python3 lnts_indir.py <cikti_dizini> <ilk_cilt> <son_cilt>
Her cilt <cikti_dizini>/v<N>.txt olarak yazılır (sayfalar \\f ile ayrılır); PDF silinir.
"""
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pymupdf

URL = "https://treaties.un.org/doc/Publication/UNTS/LON/Volume%20{n}/v{n}.pdf"


def cilt(n, dizin):
    txt = os.path.join(dizin, f"v{n}.txt")
    if os.path.exists(txt):
        return n, "var"
    pdf = os.path.join(dizin, f"v{n}.pdf")
    for deneme in range(4):
        try:
            with urllib.request.urlopen(URL.format(n=n), timeout=180) as r, open(pdf, "wb") as f:
                f.write(r.read())
            break
        except Exception as e:  # ağ hatasında üstel bekleme
            if deneme == 3:
                return n, f"hata {e}"
            time.sleep(2 ** (deneme + 1))
    d = pymupdf.open(pdf)
    metin = "\f".join(p.get_text() for p in d)
    d.close()
    open(txt, "w").write(metin)
    os.remove(pdf)
    return n, f"{len(metin)} karakter"


if __name__ == "__main__":
    dizin, ilk, son = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    os.makedirs(dizin, exist_ok=True)
    with ThreadPoolExecutor(4) as ex:
        for n, durum in ex.map(lambda n: cilt(n, dizin), range(ilk, son + 1)):
            print(n, durum, flush=True)
