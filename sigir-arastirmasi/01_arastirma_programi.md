# Araştırma Programı: Cumhuriyet Türkiyesi'nde Sığır Asamblajı (1923–1950)

Süreli yayın taraması için çok aşamalı program. Her faz kendi içinde biter; bir faz kapanınca `04_ilerleme_takibi.md` güncellenir ve bir sonrakine geçilir.

İlkeler:

1. **Seçki değil, tam tarama.** Her kaynak için "tarandı" demek, tanımlanmış anahtar kelime setinin tamamının (bkz. `02_anahtar_kelime_tezaurusu.md`) o kaynağın bütün yıllarında çalıştırılmış olması demektir. Bulunan her ilgili haber `03_kayit_sablonu.csv` biçiminde kaydedilir; eleme kayıttan **sonra** yapılır (alan: `ilgi_derecesi`).
2. **Arama ve göz taraması birlikte.** OCR'lı dönemde (1928 sonrası Latin harfli basın) anahtar kelime araması yapılır. OCR'sız veya kötü OCR'lı kaynaklarda (1923–1928 Osmanlıca basın, mikrofilm yerel gazeteler) **olay takvimine** (§4) bağlı tarih pencereleri sayfa sayfa gözle taranır.
3. **Her aramanın kaydı tutulur.** Hangi veritabanında, hangi sorguyla, hangi tarih aralığında, kaç sonuç çıktığı `05_arama_gunlugu.csv` dosyasına yazılır. Böylece "bu kaynak tamamlandı" iddiası denetlenebilir olur ve aynı sorgu iki kez çalıştırılmaz.
4. **Dört strand etiketi.** Her kayıt bir veya birden fazla strand ile etiketlenir: `S1` üreme/ırk ıslahı, `S2` yem/açlık/metabolizma, `S3` hastalık/veteriner/sınır, `S4` ahır-ev/birlikte yaşam. Genel/çapraz kayıtlar `S0` (FVADC, genel hayvancılık politikası, istatistik, uzman ağları).

---

## 1. Fazlar ve iş paketleri

| Faz | İş paketi | Kapsam | Yöntem | Tahmini süre | Bitirme ölçütü |
|---|---|---|---|---|---|
| **0** | Altyapı | Erişimlerin açılması (Gaste Arşivi aboneliği, TBMM Açık Erişim, Milli Kütüphane okuyucu kartı), tezaurusun pilot testi | 1938 yılı Cumhuriyet'te 20 çekirdek terimin OCR varyantlarıyla denenmesi; isabet/gürültü oranına göre tezaurusun düzeltilmesi | 1–2 hafta | Tezaurus v1.1 donduruldu; kayıt şablonu sabitlendi |
| **1** | Hukuki ve parlamenter iskelet | TBMM Zabıt Ceridesi / Tutanak Dergisi (1923–1950), Resmî Gazete, Düstur, kanun layihaları ve encümen mazbataları | Tam metin arama (tutanaklar 1920'lerden itibaren Latin harfli transkripsiyonla erişilebilir); her kanun için görüşme tutanakları + bütçe görüşmelerinde Ziraat Vekâleti faslı | 3–4 hafta | Her yılın Ziraat Vekâleti bütçe müzakeresi okunmuş; ilgili kanunlar (§4) listelenmiş |
| **2A** | Ulusal gazeteler — resmi hat | *Hâkimiyet-i Milliye* (1920–1934) → *Ulus* (1934–) | 1928–1950 tam anahtar kelime taraması; 1923–1928 olay pencereleri göz taraması | 4–6 hafta | Tüm tezaurus × tüm yıllar çalıştırıldı |
| **2B** | Ulusal gazeteler — İstanbul basını | *Cumhuriyet* (1924–), *Akşam* (1918–), *Vakit* / *Kurun* (1934–38 arası Kurun adıyla), *Milliyet* (1926–1935) → *Tan* (1935–1945), *Son Posta* (1930–), *Yeni Sabah* (1938–), *Vatan* (1940–), *Tasvir(-i Efkâr)* (1940'lar) | Aynı | 8–12 hafta (gazete başına 1–2 hafta) | Her gazete için arama günlüğü tam |
| **2C** | FVADC yoğun penceresi | Tüm ulusal gazetelerde kongre hazırlık, toplantı ve sonrası dönemi | **Sayfa sayfa göz taraması** (anahtar kelimeden bağımsız); kongre tarihi kesinleştirildikten sonra ±3 ay | 2–3 hafta | Pencere içindeki her sayı açılmış |
| **3** | Mesleki ve bilimsel dergiler | Veteriner, ziraat, zootekni, YZE yayınları, Ziraat Vekâleti neşriyatı (bkz. `06_kaynak_envanteri.md` §B) | İçindekiler dökümü → ilgili makalelerin tam kaydı; yazar ve atıf ağı notlanır | 6–8 hafta | Her derginin tüm sayılarının içindekiler dökümü çıkarıldı |
| **4** | Halkevi dergileri ve köy monografileri | *Ülkü* ve il halkevi dergileri; köy monografileri; etnografik anketler | İçindekiler dökümü + tam okuma (S4 için ana kaynak) | 6–8 hafta | Her dergi için döküm tamam |
| **5** | Yerel gazeteler | Milli Kütüphane mikrofilmleri; öncelik: sınır illeri (S3) ve hara/çiftlik bölgeleri (S1–S2) | Olay takvimi pencereleri + il bazlı göz taraması | Uzun vadeli, il başına 1–2 hafta | Öncelikli iller listesi (§3) bitti |
| **6** | İngilizce basın ve süreli yayınlar | İngiliz, ABD, Avustralya/YZ gazeteleri; İngilizce ticari, konsolosluk ve bilimsel yayınlar | Tam metin arama (İngilizce tezaurus) | 4–6 hafta | Her veritabanı için arama günlüğü tam |
| **7** | Uluslararası kurum yayınları | Milletler Cemiyeti, Office International des Épizooties (OIE), Uluslararası Tarım Enstitüsü (IIA, Roma), FAO (1945–) | Seçici: yalnızca Türkiye + sınır/karantina/hayvan hareketliliği | 3–4 hafta | Türkiye maddeleri listelendi |
| **8** | Eğitim materyali ve edebiyat | Ders kitapları, köylüye broşürler, radyo konuşmaları metinleri; romanlar, hikâyeler, köy yazını | Bibliyografik dökümden seçip tam okuma | Sürekli | — |

**Önerilen sıra:** 0 → 1 → 2C → 2A → 2B → 3 → 4 → 6 → 5 → 7 → 8.
Gerekçe: Faz 1 kanun ve olay takvimini sağlamlaştırır; bu takvim 2C ve 2A–B'deki göz taraması pencerelerini belirler. FVADC tezin çekirdek arşivi olduğu için 2C erkene alındı.

---

## 2. Gazete taramasında dönemlere bölme

Her gazete aşağıdaki beş dilime ayrılır; her dilim ayrı bir iş birimidir ve ilerleme tablosunda ayrı işaretlenir.

| Dilim | Yıllar | Özellik | Yöntem |
|---|---|---|---|
| D1 | 1923–Kasım 1928 | Arap harfli basın; OCR yok ya da güvenilmez | Olay takvimi pencereleri göz taraması; Osmanlıca terim listesi (tezaurus §H) |
| D2 | Aralık 1928–1933 | Harf devrimi sonrası; 1929 buhranı, 1931 Ziraat Kongresi | Tam anahtar kelime; eski imla varyantları (â, î, û; "sun'î", "mer'a") |
| D3 | 1934–1939 | Etatizm, YZE, FVADC, Hatay | Tam anahtar kelime + 2C penceresi |
| D4 | 1939–1945 | Savaş ekonomisi, Millî Korunma, et/süt kıtlığı, ordu iaşesi | Tam anahtar kelime; "iaşe", "narh", "et buhranı" eklenir |
| D5 | 1946–1950 | Çok partili dönem, Marshall Planı, traktör, FAO | Tam anahtar kelime; "Marshall", "FAO", "Amerikan mütehassıs" eklenir |

---

## 3. Coğrafi öncelikler (yerel basın ve il raporları)

**S3 — sınır ve göç hattı:** Kars, Ardahan (Kars'a bağlı), Iğdır/Doğubayazıt (Ağrı), Van, Hakkâri, Siirt, Mardin (Nusaybin, Cizre), Urfa (Ceylanpınar, Akçakale), Gaziantep (Kilis), Hatay (1939 sonrası), Diyarbakır, Erzurum.

**S1–S2 — hara, çiftlik ve ıslah merkezleri:** Bursa (Karacabey), Eskişehir (Çifteler), Malatya (Sultansuyu), Adana (Çukurova), Konya, Ankara (Orman Çiftliği, YZE), İstanbul (Pendik), Kırklareli/Edirne (boz ırk, Trakya), Kars/Erzurum (Doğu Anadolu kırmızısı).

**S4 — köy monografisi ve halkevi yoğunluğu:** Ankara köyleri, Balıkesir, Çorum, Afyon, Isparta, Konya, İzmir; Doğu illerinde kış ahırı (tam/dam) mimarisinin görüldüğü Erzurum–Kars–Van hattı.

---

## 4. Olay takvimi (göz taraması pencereleri için)

Her olay için gazetelerde **olaydan 2 hafta önce – 4 hafta sonra** penceresi göz taranır. "Doğrulanacak" işaretli tarihler Faz 1'de TBMM ve Resmî Gazete'den kesinleştirilecek.

| Tarih | Olay | Strand |
|---|---|---|
| Şubat–Mart 1923 | İzmir İktisat Kongresi (aralık öncesi, arka plan) | S0 |
| Mart 1924 | 442 sayılı Köy Kanunu, ahır–oda arası duvar zorunluluğu (kabul ve Resmî Gazete tarihleri Faz 1'de doğrulanacak) | S4 |
| 1924 | Bursa'daki Çiftlikât-ı Hümâyun'un Karacabey Harası'na dönüştürülmesi | S1 |
| 1925 | Avusturya'dan Karacabey'e Montafon sığırı getirilmesi; iç bölgelerde sığır vebasının söndürüldüğünün ilanı | S1, S3 |
| 1925 | Aşar vergisinin kaldırılması | S0 |
| 1926 | Hudut baytarlığı teşkilatı; Mardin Serum Laboratuvarı | S3 |
| 3 Mayıs 1928 | 1234 sayılı Hayvanların Sağlık Zabıtası hakkında Kanun | S3 |
| 1928 | Kuraklık ve kıtlık (Orta Anadolu), hayvan kırılması | S2 |
| 1929–1930 | Dünya buhranı, hayvan fiyatlarının çöküşü | S0, S2 |
| 1930 | Umumi Hıfzıssıhha Kanunu; Türk Baytarlar Cemiyeti'nin kuruluşu (6 Şubat 1930) ve mecmuanın ilk sayısı (1 Ekim 1930) | S3, S4 |
| 14 Ocak 1931 | Birinci Ziraat Kongresi (Ankara), ihtisas raporları | S0, S1, S2 |
| 1931 | Hayvanlar Vergisi Kanunu (tarih doğrulanacak) | S0 |
| 30 Ekim 1933 | Yüksek Ziraat Enstitüsü'nün açılışı | S1, S2 |
| 1933–1939 | Walter Spöttel'in YZE Zootekni Enstitüsü müdürlüğü | S1, S2 |
| 1934 | İskân Kanunu (göçebe aşiretlere ilişkin maddeler) | S3 |
| 1937 | Dersim harekâtı dönemi; Toprak Kanunu tartışmaları | S3, S0 |
| 1938 | **Birinci Köy ve Ziraat Kalkınma Kongresi (Ankara)**. Kesin tarih doğrulanacak; bir kaynak açılışın Başvekil Celal Bayar tarafından 27 Aralık 1938'de yapıldığını söylüyor. Gazetelerde 1938'in tamamı + Ocak–Mart 1939 taranmalı | S0–S4 |
| 1939 | Hatay'ın katılımı (Suriye sınırının yeniden çizilmesi) | S3 |
| 1940 | Köy Enstitüleri Kanunu; Millî Korunma Kanunu | S4, S2 |
| 1941 | Pamuk Kongresi (2 Ocak 1941): pamuk tohumu küspesi ve yem bağlantısı | S2 |
| 1942–1944 | Et ve süt narhı, ordu iaşesi, hayvan ihracatı yasakları | S2 |
| 1945 | Çiftçiyi Topraklandırma Kanunu | S0 |
| 1946–1948 | FAO üyeliği (yıl doğrulanacak); Marshall Planı; YZE fakültelerinin Ankara Üniversitesi'ne devri (1948) | S0, S1 |

---

## 5. İş akışı (her kaynak için)

1. Kaynağı `06_kaynak_envanteri.md` içinden seç; erişim yolunu ve OCR durumunu not et.
2. `05_arama_gunlugu.csv` dosyasına bir satır aç: kaynak, dilim, sorgu, tarih aralığı.
3. Tezaurustaki **çekirdek terimleri** (her strandda ★ işaretli) tüm OCR varyantlarıyla çalıştır.
4. Çekirdek terimlerle gelen sonuçlardan **yeni terimler** çıkarsa (yer adı, kişi adı, kurum adı, yerel ifade) tezaurusa "türetilmiş terim" olarak ekle ve onları da çalıştır.
5. Her ilgili sonucu `03_kayit_sablonu.csv` biçiminde kaydet; sayfa görüntüsünü `KAYNAK_YYYYMMDD_sSAYFA.jpg` adıyla indir.
6. Dilim bitince `04_ilerleme_takibi.md` içinde işaretle; sonuç sayısını ve gürültü oranını not et.
7. Her fazın sonunda: kişi, kurum ve yer adlarından **ağ listesi** çıkar (uzman ağları bölümü için).

---

## 6. Kişi ve kurum takibi (uzman ağları)

Başlangıç listesi; taramada çıkan yeni isimler eklenecek.

- **YZE (1933–1948):** Friedrich Falke (ilk rektör), Max Gebhardt (Veteriner Fakültesi ilk dekanı), Walter Spöttel (Zootekni Enstitüsü, 1933–1939). Diğer Alman ve Türk öğretim üyeleri ile asistan, çevirmen ve doktora öğrencileri (1933–1948 arasında 76 doktora) YZE yayın dizilerinden ve personel listelerinden çıkarılacak.
- **Kurumlar:** Ziraat Vekâleti (Baytari Umum Müdürlüğü, Zootekni Şubesi), Pendik Veteriner Bakteriyoloji ve Serum Enstitüsü, Etlik Merkez Veteriner Bakteriyoloji, Mardin Serum Laboratuvarı, Karacabey / Çifteler / Sultansuyu / Çukurova / Konya haraları, Gazi (Atatürk) Orman Çiftliği, Devlet Ziraat İşletmeleri, Türk Baytarlar Cemiyeti, Halkevleri, Köy Enstitüleri.
- **Uluslararası:** Office International des Épizooties (Paris), Milletler Cemiyeti Sağlık Teşkilatı, Institut International d'Agriculture (Roma), FAO (1945–).

Her isim için gazetelerde ad araması yapılır (Türkçe basında Alman isimlerinin imla varyantlarıyla: örn. "Spöttel / Şpötel / Spotel").
