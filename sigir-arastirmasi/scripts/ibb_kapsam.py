"""İBB Atatürk Kitaplığı (katalog.ibb.gov.tr/yordam) e-süreli yayın kapsamını çıkarır.

Her başlık için (Eser Adı alanında) e-Süreli Sayı (0505) kayıtlarının yıl dağılımını (1923–1950) yazdırır.
Kullanım: python3 ibb_kapsam.py <cikti.tsv> "Başlık 1" "Başlık 2" ...
"""
import re
import sys
import time
import urllib.parse
import urllib.request

KOK = "https://katalog.ibb.gov.tr/yordam/"


def getir(q, alttur=None):
    fq = ['kunyeAnaTurKN_str:"0505"']
    if alttur:
        fq.append(f'kunyeAltTurKN_str:"{alttur}"')
    url = KOK + "?p=1&dil=0&alan=qEser_txt&adet=50&q=" + urllib.parse.quote_plus(q) + "".join(
        "&fq[]=" + urllib.parse.quote_plus(f) for f in fq)
    with urllib.request.urlopen(url, timeout=90) as r:
        return r.read().decode("utf-8", "ignore")


def yillar(t):
    v = re.findall(r"fq\[\]=kunyeSayiYil_str%3A%22(\d{4})%22'[^>]*>[^<]*<span class='badge[^>]*>\s*([\d.]+)", t)
    return {int(a): int(b.replace(".", "")) for a, b in v}


def basliklar(t):
    import html
    return sorted({html.unescape(re.sub(r"\s*\[.*", "", x)) for x in re.findall(r'data-eseradi="([^"]*)"', t)})


if __name__ == "__main__":
    cikti = open(sys.argv[1], "w", encoding="utf-8")
    cikti.write("sorgu\tornek_basliklar\t" + "\t".join(str(y) for y in range(1923, 1951)) + "\ttoplam_1923_50\n")
    for q in sys.argv[2:]:
        t = getir(f'"{q}"')
        y = yillar(t)
        sat = [y.get(k, 0) for k in range(1923, 1951)]
        cikti.write(f"{q}\t{' | '.join(basliklar(t))[:300]}\t" + "\t".join(map(str, sat)) + f"\t{sum(sat)}\n")
        print(q, sum(sat), flush=True)
        time.sleep(1)
