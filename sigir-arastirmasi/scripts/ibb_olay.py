"""TBMM olay takvimindeki (gaste_sorgu_uret.OLAYLAR) her olay için İBB gazete sayılarını listeler.

Pencere: olaydan <once> gün önce – <sonra> gün sonra. Yalnızca Latin harfli dönem (1929+) ve
İBB'de bulunan yıllar. Çıktı ibb_gazete.py ile aynı biçimdedir; OCR için
`ibb_tarih_duzelt.py` ve `ibb_gazete.py ocr` kullanılır.

Kullanım: python3 ibb_olay.py <gazete> <liste.tsv> [--once 7] [--sonra 21] [--yillar 1929-1943]
"""
import sys
from datetime import date, timedelta

import ibb_gazete
from gaste_sorgu_uret import OLAYLAR


def main():
    gazete, cikti = sys.argv[1], sys.argv[2]
    once = int(sys.argv[sys.argv.index("--once") + 1]) if "--once" in sys.argv else 7
    sonra = int(sys.argv[sys.argv.index("--sonra") + 1]) if "--sonra" in sys.argv else 21
    y1, y2 = (sys.argv[sys.argv.index("--yillar") + 1].split("-") if "--yillar" in sys.argv
              else ("1929", "1943"))
    pencereler = open(cikti + ".pencereler", "w", encoding="utf-8")
    for tarih, olay, strand, terimler in OLAYLAR:
        d = date.fromisoformat(tarih)
        bas, bit = d - timedelta(days=once), d + timedelta(days=sonra)
        if not (int(y1) <= d.year <= int(y2)):
            continue
        pencereler.write(f"{bas}\t{bit}\t{tarih}\t{olay}\t{strand}\n")
        yillar = sorted({bas.year, bit.year})
        ibb_gazete.liste(gazete, yillar, cikti, bas.isoformat(), bit.isoformat())


if __name__ == "__main__":
    main()
