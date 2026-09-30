"""ibb_gazete.py listesindeki hatalı katalog tarihlerini sayı numarasından düzeltir.

İBB katalogunda bazı sayıların dosya adındaki tarihi yanlış (ör. Cumhuriyet 5202–5226,
Kasım 1938 olması gerekirken "1938M04.." kayıtlı). Her gazete için sayı→gün ilişkisi
komşu sayılardan (±60 sayı içindeki kayıtların medyan farkı) tahmin edilir; kayıtlı tarih
tahminden 20 günden fazla sapıyorsa tahmini tarih yazılır ve 6. sütuna "tahmini" notu düşülür.
Kullanım: python3 ibb_tarih_duzelt.py <liste.tsv> <duzeltilmis.tsv>
"""
import statistics
import sys
from collections import defaultdict
from datetime import date

satirlar = [s.rstrip("\n").split("\t") for s in open(sys.argv[1], encoding="utf-8")]
gazete = defaultdict(list)
for s in satirlar:
    if s[2].isdigit() and s[3]:
        gazete[s[1]].append((int(s[2]), date.fromisoformat(s[3]).toordinal()))

cikti = open(sys.argv[2], "w", encoding="utf-8")
duzeltilen = 0
for s in satirlar:
    s = s[:5] + [""]
    if s[2].isdigit() and s[3]:
        n, g = int(s[2]), date.fromisoformat(s[3]).toordinal()
        # ±60 sayılık pencere: ardışık 20–30 hatalı kayıttan oluşan blokları medyan dışarıda bırakır
        komsu = [gg - (nn - n) for nn, gg in gazete[s[1]] if 0 < abs(nn - n) <= 60]
        if len(komsu) >= 10:
            tahmin = int(statistics.median(komsu))
            if abs(tahmin - g) > 20:
                s[3] = date.fromordinal(tahmin).isoformat()
                s[5] = "tahmini (katalog: " + date.fromordinal(g).isoformat() + ")"
                duzeltilen += 1
    cikti.write("\t".join(s) + "\n")
print(duzeltilen, "tarih düzeltildi")
