"""Papers Past (Yeni Zelanda gazeteleri) makalelerini DigitalNZ API ile 1923–1950 arası tarar.

Kullanım: python3 digitalnz_tara.py <çıktı.csv>
Her (yıl, sorgu) çifti için bütün sayfalar çekilir; makale tam metni hem Türkiye'ye
hem sığır/hayvancılık/veteriner alanına ait bir terim içeriyorsa kaydedilir.
"""
import csv, re, sys, time
import requests

SORGULAR = [
    "turkish cattle", "turkey cattle", "anatolia cattle", "anatolian cattle", "turkish livestock",
    "turkey livestock", "rinderpest turkey", "cattle plague turkey", "foot and mouth turkey",
    "turkish peasants", "turkish peasant", "anatolian peasant", "turkish village", "anatolian village",
    "turkish agriculture", "turkey agriculture", "angora agriculture", "turkish farmers", "turkish meat",
    "turkish hides", "turkish oxen", "kurds cattle", "kurdish smuggling", "syrian frontier turkey cattle",
    "turkish veterinary", "turkey veterinary", "turkish dairy", "turkey stock breeding", "karacabey",
    "turkish nomads", "anatolia nomads", "turkish model farm", "turkey pasture",
]
TURKIYE = re.compile(r"\b(turk\w*|anatolia\w*|angora|ankara|smyrna|constantinople|istanbul|kurd\w*)\b", re.I)
ALAN = re.compile(r"\b(cattle|livestock|oxen|ox|cows?|bullocks?|bulls?|calves|heifers?|buffalo(?:es)?|rinderpest|"
                  r"cattle[- ]plague|foot[- ]and[- ]mouth|veterinar\w*|stock[- ]?breeding|stock[- ]?raising|"
                  r"pastures?|fodder|lucerne|alfalfa|silage|herds?|herdsmen|dairy|milk|butter|hides|meat|"
                  r"slaughter\w*|epizoot\w*|quarantine|nomads?|nomadic|peasants?|villagers?|manure|dung|stables?)\b", re.I)
API = "https://api.digitalnz.org/v3/records.json"


def cek(params):
    for i in range(5):
        try:
            r = requests.get(API, params=params, timeout=120, headers={"User-Agent": "academic research"})
            if r.status_code == 200:
                return r.json()["search"]
        except requests.RequestException:
            pass
        time.sleep(2 ** (i + 1))
    return {"results": [], "result_count": 0}


def main():
    goruldu = set()
    with open(sys.argv[1], "w", newline="", encoding="utf-8") as fo:
        w = csv.writer(fo)
        w.writerow(["id", "tarih", "gazete", "baslik", "sorgu", "turkiye_terimleri", "alan_terimleri", "url", "baglam", "tam_metin"])
        for yil in range(1923, 1951):
            for q in SORGULAR:
                sayfa = 1
                while True:
                    s = cek({"text": q, "and[primary_collection][]": "Papers Past", "and[year][]": yil,
                             "per_page": 100, "page": sayfa})
                    for r in s.get("results", []):
                        if r["id"] in goruldu:
                            continue
                        metin = r.get("fulltext") or ""
                        tk = sorted({m.lower() for m in TURKIYE.findall(metin)})
                        ak = sorted({m.lower() for m in ALAN.findall(metin)})
                        if not tk or not ak:
                            continue
                        goruldu.add(r["id"])
                        m = ALAN.search(metin)
                        baglam = metin[max(0, m.start() - 300): m.start() + 400]
                        w.writerow([r["id"], (r.get("date") or [""])[0][:10], ";".join(r.get("publisher", [])),
                                    r.get("title"), q, ";".join(tk), ";".join(ak), r.get("landing_url") or r.get("source_url"),
                                    baglam, metin[:20000]])
                    if sayfa * 100 >= s.get("result_count", 0) or sayfa >= 10:
                        break
                    sayfa += 1
            fo.flush()
            print(yil, len(goruldu), flush=True)


if __name__ == "__main__":
    main()
