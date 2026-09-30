"""Bir metin derlemini tezaurusla tarar ve sayfa düzeyinde isabet listesi üretir.

Kullanım: python3 tara.py <metin_klasörü> <çıktı.csv> [--meta meta.tsv]
- Klasördeki bütün .txt dosyaları (alt klasörler dahil) taranır; sayfa ayırıcı \\f.
- meta.tsv (isteğe bağlı): dosya_adı(uzantısız) <TAB> kaynak <TAB> tarih
- --parca N (isteğe bağlı): sayfa ayırıcısı olmayan metinler N karakterlik parçalara bölünür
  (sayfa sütunu bu durumda parça numarasıdır).
- Çıktı: sayfa başına bir satır; eşleşen terimler, strandlar, bağlam parçaları.
"""
import csv, os, re, sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(__file__))
from terimler import DERLENMIS, agirlik, normalize  # noqa: E402

TARIH = re.compile(r"\b(\d{1,2})\s*[-./]\s*(\d{1,2})\s*[-./]\s*(19[2-5]\d|13[34]\d)\b")


def ilk_tarih(metin):
    m = TARIH.search(metin[:3000])
    return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else ""


def main():
    kok, cikti = sys.argv[1], sys.argv[2]
    parca = int(sys.argv[sys.argv.index("--parca") + 1]) if "--parca" in sys.argv else 0
    meta = {}
    if "--meta" in sys.argv:
        for satir in open(sys.argv[sys.argv.index("--meta") + 1], encoding="utf-8"):
            p = satir.rstrip("\n").split("\t")
            meta[p[0]] = p[1:]
    dosyalar = sorted(os.path.join(d, f) for d, _, fs in os.walk(kok) for f in fs if f.endswith(".txt"))
    with open(cikti, "w", newline="", encoding="utf-8") as fo:
        w = csv.writer(fo)
        w.writerow(["dosya", "kaynak", "tarih", "sayfa", "strandlar", "terimler", "isabet_sayisi", "puan", "baglam"])
        for yol in dosyalar:
            ad = os.path.basename(yol)[:-4]
            ham = open(yol, encoding="utf-8", errors="replace").read()
            kaynak, tarih = (meta.get(ad) or meta.get(ad.split(".pdf")[0]) or [os.path.basename(os.path.dirname(yol)), ""])[:2]
            tarih = tarih or ilk_tarih(ham)
            sayfalar = ham.split("\f")
            if parca:
                sayfalar = [s[i:i + parca] for s in sayfalar for i in range(0, max(len(s), 1), parca)]
            for no, sayfa in enumerate(sayfalar, 1):
                metin = normalize(sayfa)
                bulunan = OrderedDict()
                for etiket, strand, rx in DERLENMIS:
                    for m in rx.finditer(metin):
                        bulunan.setdefault((strand, etiket), []).append(m.start())
                if not bulunan:
                    continue
                konumlar = sorted({p for ps in bulunan.values() for p in ps})
                parcalar, son = [], -10**9
                for p in konumlar:
                    if p - son > 400 and len(parcalar) < 4:
                        parcalar.append(metin[max(0, p - 200): p + 250].strip())
                        son = p
                w.writerow([ad, kaynak, tarih, no,
                            ";".join(sorted({s for s, _ in bulunan})),
                            ";".join(e for _, e in bulunan),
                            sum(len(v) for v in bulunan.values()),
                            round(sum(agirlik(e) for _, e in bulunan), 1),
                            " … ".join(parcalar)])


if __name__ == "__main__":
    main()
