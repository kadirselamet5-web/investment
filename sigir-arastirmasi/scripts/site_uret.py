"""Araştırma takip sitesini (site/index.html) depodaki dosyalardan üretir.

Okur: araştırma programı ve ilerleme dosyaları, bulgular/ raporları ve CSV'leri, 09_gorevler.json,
10_kisi_kurum.json ve (varsa) çalışma dizinindeki İBB gazete OCR isabetleri.
Yazar: site/index.html (tek dosya; veri gömülü) ve bulgular/fvadc_gazete_isabetleri.csv,
bulgular/ibb_sayi_listesi.tsv (gazete sayılarının PDF bağlantıları).

Kullanım: python3 site_uret.py [--calisma <scratchpad>]
"""
import csv
import glob
import html
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

csv.field_size_limit(10 ** 8)
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALISMA = (sys.argv[sys.argv.index("--calisma") + 1] if "--calisma" in sys.argv
           else "/tmp/claude-0/-home-user-investment/2b1f090e-69c9-53b7-8092-5187a32e1a7e/scratchpad")
BAGLAM = 280
ATLA = re.compile(r"Kapsam|yöntem|Sınırlılık|Değerlendirme", re.I)  # bulgu olmayan bölümler  # büyük tablolarda bağlam parçası uzunluğu


def oku(yol):
    p = os.path.join(KOK, yol)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def strandlar(metin):
    if re.search(r"S0\s*[–-]\s*S4", metin):
        return ["S0", "S1", "S2", "S3", "S4"]
    return ["S" + s for s in sorted(set(re.findall(r"\bS([0-4])\b", metin)))]


def md_temiz(s):
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    return re.sub(r"[*_`]", "", s).strip()


def linkler(s):
    return [{"ad": a, "url": u} for a, u in re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", s)]


# ---------------------------------------------------------------- öne çıkan kayıtlar (rapor tabloları)
def rapor_kayitlari(yol, tur, gazete_url):
    metin = oku(yol)
    kayitlar, bolum, basliklar = [], "", None
    for satir in metin.split("\n"):
        if satir.startswith("#"):
            bolum = md_temiz(satir.lstrip("#").strip())
            basliklar = None
            continue
        if not satir.startswith("|"):
            basliklar = None if not satir.strip() else basliklar
            continue
        if ATLA.search(bolum):
            continue
        hucre = [h.strip() for h in satir.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", h) for h in hucre if h):
            continue
        if basliklar is None:
            basliklar = [md_temiz(h).lower() for h in hucre]
            continue
        tum = " | ".join(hucre)
        tarih = re.search(r"\b(1[89]\d\d-\d\d-\d\d)\b", tum)
        strand_hucre = next((hucre[i] for i, b in enumerate(basliklar) if b.startswith("strand") and i < len(hucre)), "")
        st = strandlar(strand_hucre) or strandlar(tum) or strandlar(bolum)
        # başlık: "başlık"/"konu"/"olay" sütunu ya da ikinci sütun
        bi = next((i for i, b in enumerate(basliklar) if b.startswith(("başlık", "konu", "olay", "taraf"))), 1)
        baslik = md_temiz(hucre[bi]) if bi < len(hucre) else md_temiz(tum)
        gazete = ""
        m = re.search(r"\*([A-ZÇĞİÖŞÜ][^*]+)\*", bolum) if tur == "gazete" else None
        if tur == "gazete":
            gh = next((hucre[i] for i, b in enumerate(basliklar) if b.startswith("gazete")), "")
            gm = re.search(r"\*([^*]+)\*", gh) or m
            gazete = gm.group(1).strip() if gm else ""
        lk = linkler(tum)
        if tur == "gazete" and tarih and gazete:
            for g in gazete.split("/"):
                u = gazete_url.get((g.strip(), tarih.group(1)))
                if u:
                    lk.append({"ad": f"{g.strip()} PDF (İBB)", "url": u})
        kayitlar.append({
            "tur": tur, "rapor": os.path.basename(yol), "bolum": bolum, "tarih": tarih.group(1) if tarih else "",
            "yil": int(tarih.group(1)[:4]) if tarih else None, "baslik": baslik, "gazete": gazete,
            "strand": st, "metin": md_temiz(tum), "link": lk,
        })
    return kayitlar


def madde_kayitlari(yol, tur):
    """Rapor 02 gibi madde işaretli raporlar: her üst düzey madde (alt maddeleriyle) bir kayıt."""
    kayitlar, bolum, cari = [], "", None
    for satir in oku(yol).split("\n"):
        if satir.startswith("#"):
            bolum = md_temiz(satir.lstrip("#").strip())
            continue
        if re.match(r"^- ", satir) and not ATLA.search(bolum):
            if cari:
                kayitlar.append(cari)
            cari = {"bolum": bolum, "ham": satir[2:]}
        elif cari and re.match(r"^\s+(-|\S)", satir):
            cari["ham"] += " " + satir.strip().lstrip("- ")
        elif cari and not satir.strip():
            kayitlar.append(cari)
            cari = None
    if cari:
        kayitlar.append(cari)
    cikti = []
    for k in kayitlar:
        t = k["ham"]
        yil = re.search(r"\b(19[2-5]\d)\b", t)
        tarih = re.search(r"\b(19[2-5]\d-\d\d-\d\d)\b", t)
        baslik = md_temiz(re.split(r"(?<=[.:)])\s", t, 1)[0])[:220]
        cikti.append({"tur": tur, "rapor": os.path.basename(yol), "bolum": k["bolum"],
                      "tarih": tarih.group(1) if tarih else "", "yil": int(yil.group(1)) if yil else None,
                      "baslik": baslik, "gazete": "", "strand": strandlar(t), "metin": md_temiz(t),
                      "link": linkler(t)})
    return cikti


# ---------------------------------------------------------------- İBB gazete sayıları ve isabetleri
def ibb_verisi():
    listeler = sorted(glob.glob(os.path.join(CALISMA, "ibb", "*_duz.tsv")) +
                      glob.glob(os.path.join(CALISMA, "ibb", "olay", "*_duz.tsv")) +
                      glob.glob(os.path.join(CALISMA, "ibb", "dergi", "*.tsv")))
    sayilar = {}
    for yol in listeler:
        for s in open(yol, encoding="utf-8"):
            p = s.rstrip("\n").split("\t")
            if len(p) >= 5 and p[3] and p[4]:
                sayilar[(p[1], p[3], p[2])] = p[:6] + [""] * (6 - len(p[:6]))
    kalici = os.path.join(KOK, "bulgular", "ibb_sayi_listesi.tsv")
    if sayilar:
        with open(kalici, "w", encoding="utf-8") as f:
            f.write("demirbas\tgazete\tsayi\ttarih\tpdf_url\ttarih_notu\n")
            for k in sorted(sayilar):
                f.write("\t".join(sayilar[k][:6]) + "\n")
    elif os.path.exists(kalici):
        for s in list(open(kalici, encoding="utf-8"))[1:]:
            p = s.rstrip("\n").split("\t")
            sayilar[(p[1], p[3], p[2])] = p
    gazete_url = {}
    for (g, t, n), p in sayilar.items():
        gazete_url.setdefault((g, t), p[4])
        if g == "Vakit":
            gazete_url.setdefault(("Kurun", t), p[4])
        if g == "Kurun":
            gazete_url.setdefault(("Vakit", t), p[4])
    # OCR ilerlemesi
    ilerleme = []
    pencere_listesi = os.path.join(CALISMA, "ibb", "fvadc_liste_duz.tsv")
    if os.path.exists(pencere_listesi):
        hedef = Counter(p.split("\t")[1] for p in open(pencere_listesi, encoding="utf-8")
                        if "1938-11-15" <= p.split("\t")[3] <= "1939-02-28")
        for g, n in sorted(hedef.items()):
            d = os.path.join(CALISMA, "ibb", "metin", re.sub(r"\W+", "_", g).strip("_"))
            bitti = len(glob.glob(os.path.join(d, "*.txt"))) if os.path.isdir(d) else 0
            ilerleme.append({"is": f"FVADC penceresi: {g}", "bitti": min(bitti, n), "hedef": n})
    olay = os.path.join(CALISMA, "ibb", "olay", "cumhuriyet_duz.tsv")
    if os.path.exists(olay):
        n = sum(1 for _ in open(olay, encoding="utf-8"))
        bitti = len(glob.glob(os.path.join(CALISMA, "ibb", "olay", "metin", "*", "*.txt")))
        ilerleme.append({"is": "TBMM olay pencereleri: Cumhuriyet", "bitti": bitti, "hedef": n})
    ocr_dizin = os.path.join(CALISMA, "tbmm_ocr")
    if os.path.isdir(ocr_dizin):
        ilerleme.append({"is": "Halkevi dergileri ve yerel gazeteler (TBMM Açık Erişim OCR)",
                         "bitti": len([d for d in os.listdir(ocr_dizin) if d.startswith("11543_")]), "hedef": 49})
    # gazete sayfa isabetleri
    isabet = os.path.join(CALISMA, "ibb", "isabet.csv")
    kalici_isabet = os.path.join(KOK, "bulgular", "fvadc_gazete_isabetleri.csv")
    satirlar = []
    if os.path.exists(isabet):
        for r in csv.DictReader(open(isabet, encoding="utf-8")):
            if float(r["puan"]) < 3:
                continue
            gazete = r["kaynak"].replace("İBB Atatürk Kitaplığı: ", "")
            tarih, sayi = (r["dosya"].split("_") + [""])[:2]
            sayi = sayi.replace(".txt", "")
            url = sayilar.get((gazete, tarih, sayi), [""] * 5)[4] or gazete_url.get((gazete, tarih), "")
            satirlar.append({"gazete": gazete, "tarih": tarih, "sayi": sayi, "sayfa": r["sayfa"], "puan": r["puan"],
                             "strandlar": r["strandlar"], "terimler": r["terimler"], "pdf_url": url,
                             "baglam": r["baglam"]})
        with open(kalici_isabet, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(satirlar[0].keys()) if satirlar else ["gazete"])
            w.writeheader()
            w.writerows(satirlar)
    elif os.path.exists(kalici_isabet):
        satirlar = list(csv.DictReader(open(kalici_isabet, encoding="utf-8")))
    return gazete_url, ilerleme, satirlar


# ---------------------------------------------------------------- büyük tablolar
def tablo(yol, alanlar, donustur=None, sinir=None):
    p = os.path.join(KOK, yol)
    if not os.path.exists(p):
        return []
    cikti = []
    for r in csv.DictReader(open(p, encoding="utf-8")):
        if donustur:
            r = donustur(r)
            if r is None:
                continue
        cikti.append([r.get(a, "") for a in alanlar])
        if sinir and len(cikti) >= sinir:
            break
    return cikti


def kisalt(s, n=BAGLAM):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[:n] + "…"


def md_tablo(metin, baslik_deseni):
    """Markdown içinde başlığı desene uyan ilk tabloyu [[hücreler]] olarak döndürür."""
    bolum, sonuc, basliklar = "", [], None
    for satir in metin.split("\n"):
        if satir.startswith("#"):
            bolum = satir
            if sonuc:
                break
            continue
        if re.search(baslik_deseni, bolum) and satir.startswith("|"):
            h = [x.strip() for x in satir.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", x) for x in h if x):
                continue
            sonuc.append(h)
    return sonuc


def main():
    gazete_url, ocr_ilerleme, gazete_isabet = ibb_verisi()

    one_cikan = (rapor_kayitlari("bulgular/01_TBMM_tutanak_bulgulari.md", "meclis", gazete_url) +
                 madde_kayitlari("bulgular/02_dergi_ve_basin_bulgulari.md", "dergi") +
                 rapor_kayitlari("bulgular/03_ingilizce_basin_bulgulari.md", "ingilizce", gazete_url) +
                 rapor_kayitlari("bulgular/04_FVADC_gazete_penceresi.md", "gazete", gazete_url))
    # rapor 01'deki sözleşme tablosu ve LNTS satırı "antlaşma" türü
    for k in one_cikan:
        if k["rapor"].startswith("01_") and "sözleşme" in k["bolum"].lower():
            k["tur"] = "antlasma"
    for i, k in enumerate(one_cikan):
        k["id"] = f"K{i + 1:04d}"

    # zaman çizelgesi: tarihli öne çıkan kayıtlar + program olay takvimi
    zaman = [{"tarih": k["tarih"], "yil": k["yil"], "baslik": k["baslik"], "tur": k["tur"], "strand": k["strand"],
              "id": k["id"], "kaynak": (k["gazete"] + " " if k["gazete"] else "") + k["rapor"]}
             for k in one_cikan if k["tarih"]]
    for h in md_tablo(oku("01_arastirma_programi.md"), r"Olay takvimi")[1:]:
        yil = re.search(r"(1[89]\d\d)", h[0])
        if yil:
            zaman.append({"tarih": "", "yil": int(yil.group(1)), "tarih_metin": md_temiz(h[0]),
                          "baslik": md_temiz(h[1]), "tur": "program", "strand": strandlar(h[2] if len(h) > 2 else ""),
                          "id": "", "kaynak": "Araştırma programı §4 olay takvimi"})
    # sözleşme tablosundaki imza tarihleri (ISO olmayan) yıl olarak eklenir
    for k in one_cikan:
        if k["tur"] == "antlasma" and not k["tarih"]:
            yil = re.search(r"(19[2-5]\d)", k["metin"])
            if yil:
                zaman.append({"tarih": "", "yil": int(yil.group(1)), "tarih_metin": yil.group(1),
                              "baslik": "Veteriner sözleşmesi: " + k["baslik"], "tur": "antlasma",
                              "strand": ["S3"], "id": k["id"], "kaynak": k["rapor"]})
    zaman.sort(key=lambda z: (z["yil"] or 0, z["tarih"] or "9999"))

    # büyük tablolar
    def kume(r):
        return {**r, "gundem_ipucu": kisalt(r["gundem_ipucu"])}
    kumeler = tablo("bulgular/tbmm_tutanak_gorusme_kumeleri.csv",
                    ["tarih", "kaynak", "pdf_sayfalar", "toplam_puan", "strandlar", "terimler", "gundem_ipucu", "pdf_url"], kume)

    def dergi(r):
        return {**r, "baglam": kisalt(r["baglam"])}
    dergiler = tablo("bulgular/dergi_isabetleri.csv",
                     ["platform", "yayin", "yil", "sayfa_veya_parca", "puan", "strandlar", "terimler", "kayit_url", "baglam"], dergi)
    ocr = tablo("bulgular/dergi_isabetleri_ocr.csv",
                ["yayin", "yil", "dosya", "pdf_sayfa", "puan", "strandlar", "terimler", "kayit_url", "baglam"], dergi)
    beyoglu = tablo("bulgular/beyoglu_fransizca_isabetler.csv",
                    ["yayin", "dosya(yil_sayi)", "terimler", "baglam", "handle_url"], dergi)
    atbm = tablo("bulgular/atbm_makale_listesi.csv", ["yil", "sayilar", "baslik", "yazar_ve_unvan_ham", "strandlar", "terimler"])
    gazeteler = [[r["gazete"], r["tarih"], r["sayi"], r["sayfa"], r["puan"], r["strandlar"], r["terimler"], r["pdf_url"],
                  kisalt(r["baglam"])] for r in gazete_isabet]
    arama = list(csv.reader(open(os.path.join(KOK, "05_arama_gunlugu.csv"), encoding="utf-8")))

    # kişi–kurum ağı
    sozluk = json.loads(oku("10_kisi_kurum.json"))["varliklar"]
    for v in sozluk:
        v["re"] = re.compile(v["desen"], re.I)
    belgeler = [(k["id"], k["baslik"], k["metin"]) for k in one_cikan]
    belgeler += [(f"ATBM{i}", r[2], " ".join(r[2:4])) for i, r in enumerate(atbm)]
    dugum = Counter()
    kenar = Counter()
    dugum_kayit = defaultdict(list)
    for bid, baslik, metin in belgeler:
        bulunan = sorted({v["id"] for v in sozluk if v["re"].search(metin)})
        for a in bulunan:
            dugum[a] += 1
            if not bid.startswith("ATBM") and len(dugum_kayit[a]) < 60:
                dugum_kayit[a].append(bid)
        for i in range(len(bulunan)):
            for j in range(i + 1, len(bulunan)):
                kenar[(bulunan[i], bulunan[j])] += 1
    ag = {"dugumler": [{"id": v["id"], "ad": v["ad"], "tur": v["tur"], "rol": v["rol"], "sayi": dugum[v["id"]],
                        "kayitlar": dugum_kayit[v["id"]]} for v in sozluk if dugum[v["id"]]],
          "kenarlar": [{"a": a, "b": b, "w": w} for (a, b), w in kenar.items()]}

    # ilerleme tabloları
    ilerleme_md = oku("04_ilerleme_takibi.md")
    gorevler = json.loads(oku("09_gorevler.json"))

    olcum = {
        "tutanak_sayfa": sum(1 for _ in open(os.path.join(KOK, "bulgular/tbmm_tutanak_sayfa_isabetleri.csv"), encoding="utf-8")) - 1,
        "tutanak_kume": len(kumeler), "dergi_parca": len(dergiler) + len(ocr), "gazete_sayfa": len(gazeteler),
        "one_cikan": len(one_cikan), "atbm": len(atbm), "arama": len(arama) - 1,
        "gorev_bitti": sum(1 for g in gorevler["gorevler"] if g["durum"] == "bitti"),
        "gorev_toplam": len(gorevler["gorevler"]),
    }

    veri = {
        "uretim": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "olcum": olcum, "ocr": ocr_ilerleme, "gorevler": gorevler,
        "md": {
            "program": oku("01_arastirma_programi.md"), "tezaurus": oku("02_anahtar_kelime_tezaurusu.md"),
            "ilerleme": ilerleme_md, "envanter": oku("06_kaynak_envanteri.md"), "bibliyografya": oku("07_tohum_bibliyografya.md"),
            "gaste": oku("08_gaste_sorgu_plani.md"), "readme": oku("README.md"),
            "r01": oku("bulgular/01_TBMM_tutanak_bulgulari.md"), "r02": oku("bulgular/02_dergi_ve_basin_bulgulari.md"),
            "r03": oku("bulgular/03_ingilizce_basin_bulgulari.md"), "r04": oku("bulgular/04_FVADC_gazete_penceresi.md"),
        },
        "one_cikan": one_cikan, "zaman": zaman, "ag": ag,
        "tablolar": {
            "kumeler": kumeler, "dergiler": dergiler, "ocr": ocr, "beyoglu": beyoglu, "atbm": atbm,
            "gazeteler": gazeteler, "arama": arama,
        },
    }
    sablon = open(os.path.join(KOK, "scripts", "site_sablon.html"), encoding="utf-8").read()
    for ad in ("marked", "d3"):  # kütüphaneler çevrimdışı çalışsın diye gömülür
        yol = os.path.join(KOK, "scripts", "vendor", f"{ad}.min.js")
        if os.path.exists(yol):
            sablon = re.sub(r'<script src="[^"]*/' + ad + r'\.min\.js"></script>',
                            lambda m: "<script>" + open(yol, encoding="utf-8").read().replace("</script", "<\\/script") + "</script>", sablon)
    js = json.dumps(veri, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    os.makedirs(os.path.join(KOK, "site"), exist_ok=True)
    cikti = os.path.join(KOK, "site", "index.html")
    open(cikti, "w", encoding="utf-8").write(sablon.replace("/*__VERI__*/null", js))
    print(cikti, round(os.path.getsize(cikti) / 1e6, 1), "MB", olcum)


if __name__ == "__main__":
    main()
