"""LNTS metinlerinde Türkiye + veteriner/hayvancılık/mera antlaşmalarını bulur.

Kullanım: python3 lnts_tara.py <metin_dizini> <cikti.csv>
Her antlaşma ("No. NNNN" başlığından bir sonrakine kadar) bir birimdir.
Hem Türkiye terimi hem alan terimi geçen antlaşmalar yazılır.
"""
import csv
import glob
import os
import re
import sys

TURKIYE = re.compile(r"\b(Turquie|Turkey|Turkish|turque|turc|Angora|Ankara)\b", re.I)
ALAN = {
    "veteriner": r"v[ée]t[ée]rinai|veterinar",
    "epizooti": r"[ée]pizoot",
    "sığır vebası": r"peste bovine|rinderpest|cattle[- ]plague",
    "şap": r"fi[èe]vre aphteuse|foot[- ]and[- ]mouth",
    "hayvan/bétail": r"b[ée]tail|live[- ]?stock|\bcattle\b|bovid|bovin|animaux vivants|live animals",
    "mera/otlak": r"p[âa]turage|pasture|grazing|transhumanc|nomad",
    "hayvan ürünleri": r"produits animaux|animal products|viandes|\bmeat\b",
    "karantina": r"quarantaine|quarantine",
}
ALAN_RE = {k: re.compile(v, re.I) for k, v in ALAN.items()}
BASLIK = re.compile(r"(?m)^\s*No\.\s*(\d{1,5})\s*\.?\s*$")


def main(dizin, cikti):
    w = csv.writer(open(cikti, "w", newline="", encoding="utf-8"))
    w.writerow(["cilt", "antlasma_no", "sayfa_ilk", "sayfa_son", "alanlar", "turkiye_sayisi",
                "alan_sayisi", "baslik_ham", "baglam"])
    toplam = 0
    for yol in sorted(glob.glob(os.path.join(dizin, "v*.txt")), key=lambda p: int(re.sub(r"\D", "", os.path.basename(p)))):
        cilt = os.path.basename(yol)[1:-4]
        sayfalar = open(yol).read().split("\f")
        birimler = {}  # no -> [ilk, son, metin parçaları]
        simdiki = "önsöz"
        for i, s in enumerate(sayfalar, 1):
            parcalar = BASLIK.split(s)
            # parcalar: [önce, no1, sonra1, no2, sonra2...]
            birimler.setdefault(simdiki, [i, i, []])
            birimler[simdiki][1] = i
            birimler[simdiki][2].append(parcalar[0])
            for k in range(1, len(parcalar), 2):
                simdiki = parcalar[k]
                b = birimler.setdefault(simdiki, [i, i, []])
                b[1] = i
                b[2].append(parcalar[k + 1])
        for no, (ilk, son, parca) in birimler.items():
            metin = " ".join(parca).replace("\n", " ")
            tr = len(TURKIYE.findall(metin))
            if not tr:
                continue
            alan = {k: len(r.findall(metin)) for k, r in ALAN_RE.items()}
            alan = {k: v for k, v in alan.items() if v}
            if not alan:
                continue
            baslik = re.sub(r"\s+", " ", metin[:500])
            m = None
            for r in ALAN_RE.values():
                m = r.search(metin)
                if m:
                    break
            baglam = metin[max(0, m.start() - 250): m.end() + 250] if m else ""
            w.writerow([cilt, no, ilk, son, ";".join(f"{k}:{v}" for k, v in alan.items()), tr,
                        sum(alan.values()), baslik, re.sub(r"\s+", " ", baglam)])
            toplam += 1
    print(toplam, "antlaşma")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
