"""Gaste Arşivi (ve benzeri ulusal gazete veritabanları) için sorgu takip listesini üretir.

Çıktı: 08_gaste_sorgu_listesi.csv. Her satır bir iş birimidir; oturumda
isabet_sayisi / acilan / ilgili / durum sütunları doldurulur.
Kullanım: python3 gaste_sorgu_uret.py ../08_gaste_sorgu_listesi.csv
"""
import csv
import sys
from datetime import date, timedelta

# ---- Blok C: çekirdek (★) terimler; (terim, strand, OCR varyantları)
CEKIRDEK = [
    ("sığır", "S0", "sigir; sıgır; siğir"),
    ("inek", "S0", "inekler; inekhane"),
    ("öküz", "S0", "okuz; öküzler"),
    ("hayvancılık", "S0", "hayvancilik; hayvancıhk"),
    ("hayvan serveti", "S0", "hayvan servetimiz; hayvan servetimizi"),
    ("Kalkınma Kongresi", "S0", "Köy ve Ziraat Kalkınma; Ziraat Kongresi"),
    ("ırk ıslahı", "S1", "irk islahi; ıslahı nesil; cins ıslahı; hayvan ıslahı"),
    ("damızlık", "S1", "damizlik; damızlık boğa"),
    ("boğa", "S1", "boga; boğalar; aygır ve boğa"),
    ("hara", "S1", "Karacabey Harası; Çifteler; Sultansuyu; Çukurova Harası"),
    ("yerli ırk", "S1", "yerli sığır; boz ırk; kırmızı ırk; esmer ırk"),
    ("Montafon", "S1", "Montafon boğa; İsviçre esmeri; Simmental; Şarole"),
    ("zootekni", "S1", "zooteknik; zootekni enstitüsü"),
    ("suni tohumlama", "S1", "sun'i telkih; suni telkih; sunî tohumlama"),
    ("iğdiş", "S1", "igdiş; kastrasyon; burma"),
    ("yem", "S2", "hayvan yemi; yem darlığı; yem buhranı"),
    ("yonca", "S2", "yoncalık; korunga; fiğ"),
    ("silo", "S2", "silaj; ensilaj"),
    ("mera", "S2", "mer'a; otlak; yaylak; kışlak"),
    ("yem bitkileri", "S2", "yem nebatları; yem nebatatı"),
    ("kuru ot", "S2", "saman; ot darlığı"),
    ("küspe", "S2", "küsbe; pamuk tohumu küspesi; kepek"),
    ("baytar", "S3", "baytarlık; baytari; baytarî"),
    ("veteriner", "S3", "veterinerlik; veteriner fakültesi"),
    ("sığır vebası", "S3", "veba-i bakarî; veba; sığır vebasi"),
    ("şap", "S3", "şap hastalığı; ağız ve tırnak"),
    ("hayvan salgını", "S3", "salgın; hayvan hastalığı; emraz-ı sariye"),
    ("karantina", "S3", "karantine; tahaffuzhane"),
    ("hudut baytarı", "S3", "hudut baytarlığı; hudut veteriner"),
    ("aşı", "S3", "serum; aşılama; Pendik; Etlik"),
    ("şarbon", "S3", "şarbon aşısı; dalak"),
    ("hayvan kaçakçılığı", "S3", "kaçak hayvan; hayvan kaçakçıları"),
    ("ahır", "S4", "ahir; ahırlar"),
    ("köy evi", "S4", "köy evleri; köy odası"),
    ("Köy Kanunu", "S4", "köy kanunu"),
    ("tezek", "S4", "tezekten"),
    ("hayvanla beraber", "S4", "hayvanlarla bir arada; hayvanlarıyla beraber"),
]

DILIM = {1929: "D2", 1934: "D3", 1939: "D4", 1946: "D5"}


def dilim(yil):
    d = "D1"
    for y, ad in sorted(DILIM.items()):
        if yil >= y:
            d = ad
    return d


# ---- Blok B: olay pencereleri (TBMM bulgularından; tarih = görüşme tarihi)
OLAYLAR = [
    ("1924-02-21", "Köy Kanunu görüşmeleri (ahır–oda duvarı, gübre, tezek)", "S4", "Köy Kanunu; ahır; gübre; köylünün mecburi işleri"),
    ("1924-03-18", "Köy Kanunu kabulü ve ilanı (442)", "S4", "Köy Kanunu; muhtar; ihtiyar heyeti"),
    ("1924-04-01", "Ziraat Vekâleti 1340 bütçesi (Pendik, Çifteler, baytar teşkilatı)", "S1;S3", "Ziraat bütçesi; Pendik; baytar"),
    ("1925-04-12", "SSCB ile hudut meraları ve geçiş anlaşması", "S3", "hudut; mera; Gürcistan; Kars"),
    ("1925-11-21", "Sığır vebası ve salgınlar sualı", "S3", "sığır vebası; salgın; şarbon"),
    ("1926-02-08", "Mandıra ve Ağıl Kanunu lâyihası", "S4", "mandıra; ağıl"),
    ("1926-04-05", "Sığır vebası zamanında sığır ve deri ithal/ihraç yasağı", "S3", "sığır vebası; deri; ihracat yasağı"),
    ("1926-06-01", "Islah-ı Hayvanat Kanunu (904) görüşmeleri", "S1", "ıslah-ı hayvanat; boğa; aygır; iğdiş; damızlık"),
    ("1927-12-10", "Kayseri pastırmalık ineklerin yolda tutulması", "S3", "pastırma; Kayseri; Develi; inek; karantina"),
    ("1928-04-26", "1234 sayılı Zabıta-i Sıhhiye-i Hayvaniye Kanunu", "S3", "hayvanların sağlık zabıtası; baytar; karantina; şap"),
    ("1929-02-16", "SSCB baytarî mukavelenamesi tasdiki", "S3", "baytarî mukavele; Rusya; Sovyet; hudut"),
    ("1929-03-04", "Mandıra ve Ağıllar Kanunu görüşmesi", "S4", "mandıra; ağıl; ağıllar kanunu"),
    ("1930-04-17", "Umumi Hıfzıssıhha Kanunu (zoonozlar, mezbaha, süt)", "S3", "hıfzıssıhha; mezbaha; süt; şarbon"),
    ("1931-03-02", "Islah-ı Hayvanat Kanunu 4. madde tadili", "S1", "ıslah-ı hayvanat; boğa"),
    ("1931-06-29", "Davar ve Ehlî Hayvanlar Vergisi", "S0", "hayvanlar vergisi; ağnam; davar"),
    ("1932-06-16", "Baytar Süreyya'nın sığır vebası aşısı sualı", "S3", "sığır vebası aşısı; Süreyya; veba"),
    ("1933-06-10", "Yüksek Ziraat Enstitüsü kanunu", "S1", "Yüksek Ziraat Enstitüsü; baytar fakültesi"),
    ("1934-05-12", "Bulgaristan baytarî mukavelenamesi", "S3", "Bulgaristan; baytarî mukavele; Milletler Cemiyeti"),
    ("1934-06-07", "İskân Kanunu (aşiret, göçebe, yaylak)", "S3", "iskân; aşiret; göçebe; yaylak"),
    ("1936-01-13", "Hayvanlar Vergisi Kanunu (damızlık, iğdiş, celep)", "S1", "hayvanlar vergisi; celep; damızlık"),
    ("1936-11-13", "Emin Draman: muhacir ailelerin ahır ve samanlıkları", "S4", "muhacir; ahır; samanlık; Yozgat"),
    ("1937-01-29", "Orman Kanunu (mera, otlatma)", "S2", "orman kanunu; otlatma; keçi; mera"),
    ("1937-05-12", "Ziraat Vekâleti teşkilat kanunu (Veteriner İşleri, Zootekni, haralar)", "S1;S3", "Ziraat Vekâleti teşkilatı; veteriner işleri; hara"),
    ("1937-06-07", "İran baytarî mukavelesi", "S3", "İran; baytarî mukavele; sığır vebası"),
    ("1937-06-12", "Atatürk'ün çiftliklerini Hazine'ye bağışlaması", "S1", "Orman Çiftliği; Atatürk çiftlikleri; hediye"),
    ("1938-03-23", "Hayvanlar Vergisi değişikliği (kaçakçılık, damızlık boğa)", "S1;S3", "hayvanlar vergisi; kaçakçılık; boğa"),
    ("1938-05-23", "Ziraat Vekâleti 1938 bütçesi (haralar, mera ıslahı, yoncalık)", "S1;S2", "ziraat bütçesi; hara; yonca; mera"),
    ("1938-12-07", "Ordudan çıkarılan hayvanların köylüye satışı", "S1", "ordu hayvanları; köylüye satış"),
    ("1939-05-15", "Yunanistan veteriner mukavelenamesi", "S3", "Yunanistan; veteriner mukavele"),
    ("1939-05-29", "Ziraat Vekâleti 1939 bütçesi (Ziraat Kongresi'ne atıflar)", "S0", "ziraat bütçesi; kalkınma kongresi; hara"),
    ("1940-06-10", "Suriye mukavelenamesi, baytarî rejim protokolü", "S3", "Suriye; baytarî; hudut; sığır vebası"),
    ("1941-04-14", "Irak veteriner mukavelenamesi", "S3", "Irak; veteriner mukavele"),
    ("1941-05-09", "Çiftçi Mallarının Korunması Kanunu", "S2", "çiftçi mallarının korunması; mera; bekçi"),
    ("1942-01-09", "Millî Korunma koordinasyon kararı: çift ve koşum sığırı ile damızlık dişi sığır ve mandanın kasaplık alım satımı yasak (yürürlük 9.1.1942; Cumhuriyet)", "S1;S2", "kesim yasağı; Millî Korunma; öküz; inek; et"),
    ("1945-05-18", "Çiftçiyi Topraklandırma Kanunu (mera, çift hayvanı)", "S2", "toprak kanunu; mera; çift hayvanı"),
    ("1945-06-08", "At vebası, hayvan öldürme ve tazminat", "S3", "at vebası; tazminat"),
    ("1945-12-27", "Tarım Bakanlığı 1946 bütçesi (hayvan kırımı)", "S2", "hayvan kırımı; hayvan zayiatı; yem"),
    ("1946-06-13", "Mısır'daki sığır vebası nedeniyle ödenek", "S3", "sığır vebası; Mısır"),
    ("1948-05-12", "Et fiyatları, canlı hayvan ihracı, hayvan sayımı", "S0", "et fiyatları; hayvan ihracı; hayvan sayımı"),
    ("1948-11-19", "Suriye sınırında sığır ve manda hırsızlığı, kaçakçılık", "S3", "hayvan hırsızlığı; hudut; kaçakçılık; manda"),
    ("1949-01-14", "Mera meselesi ve mera kavgaları", "S2", "mera; mera kavgası"),
    ("1949-04-25", "Erken kış, hayvan zayiatı, Şark'ta hayvan vaziyeti", "S2", "hayvan zayiatı; kış; yem; Şark"),
    ("1949-11-23", "Kuraklık bölgelerine yem dağıtımı", "S2", "kuraklık; yem; küspe"),
    ("1950-03-10", "İran'da sığır vebası, sirayet tedbirleri", "S3", "sığır vebası; İran; hudut"),
    ("1950-03-16", "Yayla ve meraların köylere tahsisi kanunu", "S2", "yayla; mera; köy tüzelkişiliği"),
    ("1950-03-22", "Hayvan hırsızlığı cezalarının artırılması", "S3", "hayvan hırsızlığı"),
]

# ---- Blok D: kişi ve kurum adları (tüm dönem)
ADLAR = [
    ("Spöttel", "S1", "Şpötel; Spotel; Spöttel"),
    ("Gebhardt", "S3", "Gebhart; Gebhard"),
    ("Falke", "S1", "Profesör Falke"),
    ("Yüksek Ziraat Enstitüsü", "S1", "Y. Z. E.; Ziraat Enstitüsü"),
    ("Pendik", "S3", "Pendik bakteriyolojihanesi; Pendik laboratuvarı"),
    ("Etlik", "S3", "Etlik veteriner; Etlik serum"),
    ("Karacabey", "S1", "Karacabey Harası; Karacabey merinosu"),
    ("Orman Çiftliği", "S1", "Gazi Orman Çiftliği; Atatürk Orman Çiftliği"),
    ("Sultansuyu", "S1", "Sultansuyu Harası"),
    ("Çifteler", "S1", "Çifteler Harası"),
    ("Devlet Ziraat İşletmeleri", "S1", "D. Z. İ."),
    ("Türk Baytarlar Cemiyeti", "S3", "Baytarlar Cemiyeti; Veteriner Hekimler Cemiyeti"),
    ("Muhlis Erkmen", "S0", "Ziraat Vekili Muhlis"),
    ("Şakir Kesebir", "S0", "Ziraat Vekili Şakir"),
    ("Faik Kurdoğlu", "S0", "Ziraat Vekili Faik"),
    ("Sırrı Day", "S0", "Tarım Bakanı Sırrı"),
    ("Office International des Épizooties", "S3", "Beynelmilel Epizooti Bürosu; Epizooti Ofisi"),
    ("Cavid Oral", "S0", "Tarım Bakanı Cavit Oral"),
]


def main(yol):
    w = csv.writer(open(yol, "w", newline="", encoding="utf-8"))
    w.writerow(["sorgu_no", "blok", "oncelik", "strand", "sorgu", "varyantlar",
                "baslangic", "bitis", "dilim", "gazete", "yontem", "aciklama",
                "isabet_sayisi", "acilan", "ilgili", "durum"])
    n = 0

    def satir(*a):
        nonlocal n
        n += 1
        w.writerow([f"G{n:04d}", *a, "", "", "", "[ ]"])

    # Blok A: FVADC penceresi
    for terim in ["Kalkınma Kongresi", "Ziraat Kongresi", "Köy ve Ziraat", "kongre hayvancılık",
                  "kongre sığır", "kongre baytar", "kongre mera", "kongre ahır"]:
        satir("A-FVADC", 1, "S0-S4", terim, "", "1938-06-01", "1939-03-31", "D3",
              "tümü", "anahtar kelime", "Kongre hazırlık, toplantı, komisyon raporları ve yankıları")
    for gz in ["Ulus", "Cumhuriyet", "Tan", "Akşam", "Kurun/Vakit", "Son Posta", "Yeni Sabah"]:
        for ay_bas, ay_bit in [("1938-11-15", "1938-12-15"), ("1938-12-16", "1939-01-15"),
                               ("1939-01-16", "1939-02-28")]:
            satir("A-FVADC", 1, "S0-S4", "(göz taraması)", "", ay_bas, ay_bit, "D3", gz,
                  "sayfa sayfa göz taraması", "Kongre haftası ve sonrası; anahtar kelimeden bağımsız")

    # Blok B: olay pencereleri
    for tarih, olay, strand, terimler in OLAYLAR:
        d = date.fromisoformat(tarih)
        bas, bit = d - timedelta(days=14), d + timedelta(days=28)
        yontem = "göz taraması (Arap harfli)" if d < date(1928, 12, 1) else "anahtar kelime + manşet göz taraması"
        satir("B-olay", 1 if d.year >= 1929 else 2, strand, terimler, "", bas.isoformat(), bit.isoformat(),
              dilim(d.year), "tümü", yontem, olay)

    # Blok C: çekirdek terimler × yıl (1929–1950)
    for terim, strand, var in CEKIRDEK:
        for yil in range(1929, 1951):
            satir("C-cekirdek", 2, strand, terim, var, f"{yil}-01-01", f"{yil}-12-31",
                  dilim(yil), "tümü", "anahtar kelime",
                  "İsabet sayısı çok yüksekse gazete gazete ve çeyrek yıllara bölünür")

    # Blok D: adlar
    for ad, strand, var in ADLAR:
        satir("D-ad", 3, strand, ad, var, "1923-01-01", "1950-12-31", "D1-D5", "tümü",
              "anahtar kelime", "Kişi ve kurum ağları")

    print(n, "sorgu satırı")


if __name__ == "__main__":
    main(sys.argv[1])
