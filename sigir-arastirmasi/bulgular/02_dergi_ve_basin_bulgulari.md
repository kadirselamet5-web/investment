# Dergiler, Resmî Yayınlar ve Basın (1923–1950): Tarama Bulguları — Tur 1

**Taranan derlemler:**

| Derlem | Kapsam | Yöntem | Sonuç dosyası |
|---|---|---|---|
| TBMM Kütüphanesi Açık Erişim | 1923–1950 tarihli 658 kayıt (dergi, gazete, resmî yayın). Bunların 168'inde kurumun OCR metni vardı | OCR metinleri indirilip tezaurus v1.0 ile 3.000 karakterlik parçalar halinde tarandı | `dergi_isabetleri.csv` |
| TBMM Açık Erişim, OCR'ı olmayan Latin harfli kayıtlar | 49 öncelikli kayıt (halkevi dergileri, yerel gazeteler, Berkes) | PDF'ler indirilip tesseract (Türkçe) ile OCR'landı. **Devam ediyor:** şu ana kadar Berkes, *Doğuş* (Kars) ve *Karacadağ* (Diyarbakır) bitti | `dergi_isabetleri_ocr.csv` |
| Internet Archive | 1.101 kayıt (Türkçe, 1923–1950; *Ülkü* serileri, halkevi dergileri, *Askerî Tıbbî Baytarî Mecmuası*, *Kadro* vb.) | `_djvu.txt` OCR metinleri | `dergi_isabetleri.csv` |
| *Beyoğlu* (Fransızca İstanbul gazetesi, 1939–1944) ve *La Turquie Kemaliste* | TBMM Açık Erişim | Fransızca terimlerle ayrı tarama | `beyoglu_fransizca_isabetler.csv` |

`dergi_isabetleri.csv`, puanı 3 ve üzeri olan 10.284 parçayı içerir. Sözlük, ansiklopedi, dil çalışması ve konu dışı eski metinler çıkarılmıştır. Her satırda yayın, yıl, dosya, parça numarası, eşleşen terimler, bağlam ve kayıt bağlantısı vardır. Aşağıda yalnızca okunarak seçilen öne çıkan kayıtlar yer alıyor. Tam liste CSV'dedir.

**Uyarı:** Parça numaraları OCR metni içindeki sıradır. Basılı sayfa numarası için kaynak PDF'e bakılmalıdır. Arap harfli sayılarda (ör. *Ayın Tarihi* 1923–1929, *Ziraat Vekâleti Mecmuası* 1924–25) OCR kullanılamaz durumdadır; bunlar göz taraması listesindedir (bkz. sonda).

---

## 1. *Askerî Tıbbî Baytarî Mecmuası* (1923–1937; 131 sayı)

Kaynak: [Internet Archive](https://archive.org/details/askeri-tibbi-baytari-mecmuasi) ve [TBMM Açık Erişim](https://acikerisim.tbmm.gov.tr/handle/11543/4210). S3 için ana dergi. S1 ve S2 için de önemli; 712 güçlü parça var.

- **S1 × S3, sığır vebası aşısı denemeleri (1931):** Gazi Çiftliği'nden gelen yerli "boz ırk" danalar ile "Simental, Kırım gibi ecnebi hassas ırklar" deney hayvanı olarak kullanılıyor. Serum öküzleri, virüs kontrolleri, kurutulmuş dalak aşısı, saponinli virüs aşısı (Curasson) denemeleri anlatılıyor. Parçalar p1227–1233, p1264–1265, p1360, p1474, p1543, p2073. Yerli ve yabancı ırkların hastalığa "hassasiyeti" burada deneysel bir kategori olarak kuruluyor.
- **S3, sığır vebasının Osmanlı'dan Cumhuriyet'e tarihçesi:** Mondros döneminde İstanbul ve çevresinin salgın bölgesine girmesi, baytarların köylerdeki mücadelesi (p1184). Ayrıca 1917'de Şam'da sığırlarda tripanozomiyaz (p2434).
- **S3, uluslararası bağlantılar:** Uluslararası baytarî kongreler tarihçesi (1885 Brüksel vb., p1174–1177). 1934 Uluslararası Veteriner Kongresi rapor özetleri (sığır tüberkülozu ve BCG, anaplazmoz; p2081, p2197). Türkiye'nin kongrenin daimi komitesine alınması (p1178).
- **S2, silaj ve yem bilimi:** Silajda besin kaybı, Alman şartlarında mısır silajı verimi, kuru ot yapımının zorlukları, pancar posası (p2064–2071). Bilginin Alman kaynaklarından çevrilip uyarlandığını gösteriyor.
- **S4, ahır ve hastalık:** "Sütlü inekleri kapalı ahırlarda bulundurmak" ile verem arasındaki ilişki (p2373). Ahır hıfzıssıhhası ve paratüberküloz (p765–767). Parazitlere karşı ahır dezenfeksiyonu ve gübrenin uzaklaştırılması (p2202). Köylerde gübrenin ve dışkının avlulara atılmasının yarattığı risk (p1639).
- **Uzman ağları:** Ankara'da askerî ve sivil baytarların on beş günde bir konferans düzenlemesi; neşriyat heyetinde parazitolog Naki Cevat, zooteknist Nurettin, bakteriyolog Refik ve Sadık, zooteknist Selahattin (p1173). Zootekni Enstitüsü'nde verilen konferanslar, ör. Süreyya Tahsin'in antraks salgınları konferansı (p1512). Leipzig'den Prof. Dr. Sprehn'in Ankara Baytar Fakültesi parazitoloji profesörlüğüne atanması (p1950). Derginin 10. yıl fihristi (p1678) ve konu dizinleri (p2278, p2464, p2013), makale tam listesini çıkarmak için başlangıç noktası.
- **At yetiştiriciliği karşılaştırması:** Uzunyayla aygır deposu ve suni tohumlamanın yayılması (1929 sonrası, p2244–2245).

## 2. *Ayın Tarihi* (Matbuat Umum Müdürlüğü aylık basın ve ajans derlemesi)

Kaynak: [TBMM Açık Erişim](https://acikerisim.tbmm.gov.tr/handle/11543/3935). Gazetelere doğrudan erişilemediği için en iyi **gazete vekili**. Latin OCR'lı ciltler 1937 ve 1939–1946'ya ait; 1923–1929 ciltleri Arap harfli ve OCR'sız.

- **S1, Kars (1939):** "Üç yıl önce 148 inekle işe başlamış olan" Göle inekhanesi. Vilayetin her yerinden getirilen sığırların teşhir edildiği inek ve damızlık boğa sergisinde Göle inekhanesinin Kars'ta sığır ıslahındaki başarısı (1939, sayı 71).
- **S1 × S2, kolektif boğa aşım durakları (1939):** Köy bütçelerinde biriken paradan 47 boğa satın alınıp duraklara yerleştirilmesi; istasyonların ot, saman ve arpa ihtiyacı; Eskişehir şeker fabrikasından 80 ton pancar küspesi getirilmesi (sayı 72, p32). Kütahya'da "sığır cinsinin ıslahı için 9 yerde kollektif boğa aşım durakları" kurulması (sayı 72, p31).
- **S3, ithalat yasağı (28 Nisan 1939):** Sığır vebası nedeniyle İngiliz-Mısır Sudanı'ndan ve Fransız Çinhindi'nden çift tırnaklı hayvan ve hayvan maddeleri ithalinin yasaklanması (1940 derlemesi, p43).
- **S3, göç ve hayvan (1939):** Romanya'dan Kocaeli'ye gelen 502 hanelik göçmenin yanında 1.000 baş büyükbaş ve 2.000 koyun getirmesi (sayı 72, p27). Bursa'ya yerleştirilen göçmenlere hayvan alımı; Karacabey baytar heyeti (1940).
- **S2, ihracat yasağı listeleri (Eylül 1939):** Fiğ, burçak, kepek, ot, saman, pamuk tohumu (sayı 70 ve 72).
- **S2, kırım (1945):** Tarım Bakanı: "Bu yıl Konya, Eskişehir, Polatlı ve Aksaray havzasında hayvan kırımları olmuştur… yüzde otuza, yüzde elliye kadar" (sayı 138, p166). Kombinaların meralara dokunmaması dileği (p140).
- **S3 (1943):** Tarım Bakanı'nın bütçe konuşması: salgınlarla "yüz binlerce hayvanın ölümü şeklinde bir vaka" artık olmadığı iddiası; sığır vebası (sayı 114, p90).
- **S1 (1946):** Veteriner İşleri Genel Müdürlüğü'nün hayvan ıslahı projeleri; zoolog, bakteriyolog ve bölge veteriner müdürlerinin Ankara'da toplanması (sayı 148, p6).
- **S4 (1944):** Köylünün "çamur sıvalı yer odalarında tezekle ısınmaya mahkûm" edildiği söylemi (sayı 127, p55).
- **S0:** 1929 sayım vergisi tarifeleri (öküz ve inek 125 kuruş; sayı 57–59). 1941'de hayvanlar vergisine yapılan zamlar (sayı 90).

## 3. *Ülkü* (1933–1950; üç seri) ve Halkevi yayınları

Kaynak: [TBMM Açık Erişim](https://acikerisim.tbmm.gov.tr/handle/11543/4086) ve Internet Archive ([Seri 1](https://archive.org/details/ulku_halkevleri_mecmuasi_seri_1), [Seri 2](https://archive.org/details/ulku_milli_kultur_dergisi_seri_2), [Seri 3](https://archive.org/details/ulku_milli_kultur_dergisi_seri_3)).

- **S1, Cumhuriyet'in 15 yılı bilançosu (Ülkü, sayı 69, Aralık 1938):** Haralar; Çifteler, Uzunyayla, Mercimek, Akçadağ, İnanlı ve Diyarbakır aygır depoları; haralardaki 2.547 baş sığır; "yabancı memleketlerden boğalar getirilerek köylere dağıtılmıştır, bunların yekûnu 4.264 başa çıkmıştır". Yazar "ideal olan öküz değil, beygir olmalıdır" diyor (p24–28 / Seri 1 p4978–4979).
- **S1 × S3, ithal ırk ve hastalık (Ülkü Seri 1, p7247):** "Yavru atma salgını, meme iltihabı salgını gibileri de damızlık olarak yabancı memleketlerden getirttiğimiz kültür ırklar vasıtasıyla anayurda sokulmuş yabancı hastalıklardır."
- **S4, hayvan barınağı (Ülkü Seri 1, p7248):** "Ahır, ağıl ve kümes dediğimiz hayvan meskeni memleketimizde hemen hemen hiç yok gibi bir şeydir."
- **S4, köy monografileri:**
  - Haymana, Ahırlı köyü öğretmeni Osman Nuri (1933): koç, boğa ve aygır temini ve "fennî ahırlarda" beslenmeleri; köy evlerinin badanası (Seri 1 p1280–1281).
  - 1933: bir köyde "ahırlar evlerden ayrı" (p1280).
  - Karadeniz fındık bölgesinde bir köy (1949, sayı 29): "Köy evleri dağınıktır… ahırlar evlerin altındadır."
  - Karadeniz fındık bölgesi (1941–46): yataklık, gübrelik, ahır bakımı (Seri 2 p4498; 1946 sayı 106).
  - 1946, sayı 106: çocukların buzağı ve tosun gütmesi.
  - 1946, sayı 108: bir köyde "sığır cinsi iyice ıslah edilmiş, 8–16 litre süt veren inekler".
  - 1946, sayı 120: manda koşumunun at koşumuna geçişi ve öküzün nadasta tutulması.
- **S2 (1947):** Köylülerin samanın yem değeri olmadığını bilmesine karşın yeterli yem yetiştirmemesi (Seri 3 p2226).
- **S0 (1935):** Hayvanlar vergisi kayıtlarına göre 1934'te 7.389.816 büyükbaş hayvan (sayı 29).
- **Çorum (1934):** 4 yıl önce Balya'dan boğaların ıslahı için 6 boğa getirilmesi; aygır ve tay sayıları (sayı 21).

**Halkevi dergileri:**
- ***Altıok / 6 Ok* (Edirne, 1933–34), S4 için çekirdek alıntı:** "Köy Kanunu 14. madde… ahırlarımızı odalarımızdan ayrı yerlerde yapmak… Eğer hayvanlarımızı odalarımızda yatırır veyahut biz hayvanlarımızın ahırlarında yatacak olursak bizim hayvanlardan ne farkımız vardır?" Ayrıca tetanoz ile gübre ilişkisi ve ahır ısısı tablosu (sütlü inekler için 14–16 derece) ([he-6ok](https://archive.org/details/he-6ok); TBMM [11543/4014](https://acikerisim.tbmm.gov.tr/handle/11543/4014)).
- ***Altın Yaprak* (Bafra, 1936) köy monografileri, S4:** "Evlerin %70'i iki katlı… alt katında ahır, tütün kuyusu vardır. Bir katlı evler bir odalıdır; ahır ayrıdır." Köylerin hayvan sayıları; "bu hayvanlara fennî bir şekilde bakılmamaktadır" ([he-altin-yaprak](https://archive.org/details/he-altin-yaprak)).
- ***Muğla Halkevi Dergisi* (1937–38), S1, S2, S4 ve eğitim materyali:** Baytar Selim Yatağan'ın "Sığır yetiştiriciliği, ıslah ve bakım hakkında öğütler" dizisi (kızgınlığın tespiti, beslenme, sığır ahırlarının planı, yemlikler, sidik arığı, dişle yaş tayini). TBMM [11543/4323](https://acikerisim.tbmm.gov.tr/handle/11543/4323).
- ***Altan* (Elazığ, 1935), S1:** "Damızlığa yaramayan tosun, koç, teke gibi hayvanları iğdiş yapmak için yedi adet burdizzo" getirilmesi ve köylüye kullanımının öğretilmesi; Sultansuyu Harası damızlıkları; ruam şahadetnamesi ([11543/4012](https://acikerisim.tbmm.gov.tr/handle/11543/4012)).
- ***Konya* Halkevi dergisi:**
  - 1942: "Sığır, koyun, keçi, at gibi demirbaş hayvanlar buralarda dejenere olmuştur… cins boğa…" (S1).
  - 1942: Kışlık yem hazırlığı öğütleri (S2).
  - 1943: Vilayette 17.039 sığıra şarbon aşısı; OCR'da "ağranıanadan" diye okunan bir hastalıktan her yıl telef olan yüz bin hayvanın tedaviyle kurtarıldığı iddiası; Konya Harası aygır deposu; yem tohumu dağıtımı (Kayseri yoncası, korunga) ([11543/4310](https://acikerisim.tbmm.gov.tr/handle/11543/4310)).
- ***Karacadağ* (Diyarbakır Halkevi, 1938–41; tesseract OCR):**
  - **S3 × S1:** Birinci Umumi Müfettişlik veteriner müşaviri Nurettin Aral, "Memleketimizin millî hayvan yetiştirme siyaseti ne olmalıdır" (1940).
  - **S3:** Cenup mıntıkası yetiştirme mütehassısı Dr. Veteriner Mithat Özdoğan'ın göçmen köylerinde zirai tetkik raporu (1940). Göçmen köylerinin öküz, inek ve manda sayıları; iskân edilenlere "birer çift koşum öküzü" verilmesi (Bismil, 1941).
  - **S3, dikkat çekici:** Halkevinin köylerde düzenlediği Türkçe ve yurt bilgisi yarışmalarında kazanan köylülere ödül olarak öküz, inek ve tosun verilmesi (1939). Hayvan, dil ve vatandaşlık politikasının aracı olarak kullanılıyor.
  - **S1 (1939):** "Bu kara sığırların da ıslahı lazımdır."
  - Diyarbakır'ın sığır ve deri ihracatı (1939). TBMM [11543/4315](https://acikerisim.tbmm.gov.tr/handle/11543/4315).
- ***Doğuş* (Kars Halkevi, 1938–39; tesseract OCR):** Kars'ta hayvancılık; İran koyunları, Gürcü koyunları, sığırlar ([11543/4291](https://acikerisim.tbmm.gov.tr/handle/11543/4291)).
- ***Burdur Halkevi Dergisi* (1941), S4:** Köy odası şiiri: "Sağında bir ahır, solda samanlık" ([11543/3939](https://acikerisim.tbmm.gov.tr/handle/11543/3939)).
- ***Uludağ* (Bursa Halkevi):** Merinos koyunculuğu ve Karacabey (1935); Karacabey sel felaketi (1940).

## 4. Resmî metinler: *Düstur* (3. tertip) ve kanun metinleri

Kaynak: [TBMM Açık Erişim](https://acikerisim.tbmm.gov.tr/handle/11543/4088). Tutanaklarda görüşülen kanunların yürürlükteki metinleri.

- **S1:** *Islah-ı Hayvanat Kanunu*, No. 904, 7 Haziran 1926 (Resmî Ceride 29 Haziran 1926, sayı 407): "Aygır ve boğa sahibi olan her fert bulunduğu köy veya mahalle ihtiyar meclisine her aygır veya boğa…" Islah-ı hayvanat komisyonları, nesilname komisyonu, mükâfat ve madalyalar; emlâk-ı milliyedeki meraların damızlık yetiştirenlere tercihen kiralanması; hara, inekhane, ağıl ve aygır depolarının kurulması.
- **S1:** Karacabey Harası talimatnamesi: "memleketin mevcut hayvanat-ı ehliyesinin ıslahına elverişli yerli ve ecnebi halis-üd-dem veya nısf-üd-dem damızlık hayvanat-ı feresiye, bakariye, ganemiye ve maziye ve tuyur-ı ehliye yetiştirilir".
- **S3:** Türkiye–SSCB baytarî mukavelenamesi (Batum'da 28 Ocak 1927'de parafe edildi, Ankara'da 6 Ağustos 1928'de imzalandı). Sınırdan meraya geçen sürüler için cüzdanlar ve listeler, hudut baytarına 3 gün önceden haber verme, 8 günlük şahadetnameler, sığır vebası görülürse serum ve karantina, "hududu geçecek hayvan sahiplerine verilen vesika" örneği.
- **S3:** 1234 sayılı kanunun ihbarı zorunlu hastalık listesi (sığır vebası "veya malkıran", şap "veya tabak hastalığı"); ruam ve itlaf maddeleri. Ayrıca 405 sayılı (1340) Muayene-i Hayvaniye Resmi kanunu.
- **S4:** Köy Kanunu'nun köylünün isteğine bağlı işler listesi: "köye ortaklama korucu, sığırtmaç, danacı ve çoban tutmak", bulaşıcı hastalıkların hükümete bildirilmesi.
- **S0:** Sayım vergisi tarifeleri (1926: inek ve öküz 80 kuruş; 1929: 125 kuruş); demiryolu hayvan nakliye tarifeleri; Suriye ile gümrük tarifeleri.

## 5. Diğer dergiler

- **Birinci Köy ve Ziraat Kalkınma Kongresi, *Komisyonlar Mazbatası* (1938)** ([11543/2468](https://acikerisim.tbmm.gov.tr/handle/11543/2468)). Hayvan İşleri Komisyonu kararları:
  - sayım vergisinin kaldırılması, mezbaha ücretinin indirilmesi, yetiştiricilere krediyle tuz verilmesi;
  - "salma ve bozuk ismiyle hayvanatın başıboş olarak" yem ekili yerlerde gezmesinin önlenmesi;
  - yoncalıklara 3 yıl arazi vergisi muafiyeti;
  - dana besleme istasyonları ve kooperatifleri, hayvan sigortası;
  - Urfa, Mardin ve Diyarbakır'da Arap atı tescili;
  - "yeniden kaleme alınmış İslah-ı Hayvanat Kanunu"nun yürürlüğe girmesi; tenasül biyolojisi araştırmaları;
  - mezbahalarda muayenenin veterinerlerce yapılması, 405 sayılı muayene resminin kaldırılması.

  Kongre raporlarıyla karşılaştırılmalı.
- ***Halk Bilgisi Haberleri* (1929–1940'lar), S4 için etnografik ev tarifleri:**
  - 1934: "Kapıdan girilince solda bir kapı görülür. Bu kapı dam kapısıdır… inekler için yapılmış ayrı bir yer… inek mahalli ahırlarda hatıllarla zeminden iki karış kadar yükseltilmiş… At ve eşek için ayrılan yer doğrudan doğruya topraktır"; "evler birinci ahır katından sonra ekseriyetle bir katlıdır".
  - 1936: Çocuğun süt dişinin "malı inek, öküz, koyun cihetinden zengin olması" için hayvan ahırına atılması.

  TBMM [11543/4019](https://acikerisim.tbmm.gov.tr/handle/11543/4019); IA koleksiyonu `halk-bilgisi-haberleri`.
- ***Kadro* (1932–34), S2/S4:** "Gübreyi tezek halinde tandırda yakan ve tarlası yorulunca meradan veya ormandan bir yenisini açan İç Anadolu köylüsü"; "Dünyanın en talihsiz, en bakımsız hayvanları bizim topraklarımızda yaşarlar"; Kars, Ardahan, Erzurum ve Bayazıt yaylalarında ticari hayvancılık ([IA](https://archive.org/details/kadro-dergisi-01-36-sayilari)).
- ***Atayolu* gazetesi (1948–49):**
  - "Türk veterinerliğinin 106. yılı" (Veteriner Fikri Üstün): "İmparatorluk devrinde veterinerlerin elinde yalnız bir sığır vebası serumu var(dı)"; köylünün veterinere güveni.
  - Bozöyük Harası hayvan sergisi (97 inek, boğa ve dana).
  - Devlet Ziraat İşletmeleri Hatay çiftliğinde yetiştirilen "cenup kırmızısı" sığırların satışı.

  [11543/4288](https://acikerisim.tbmm.gov.tr/handle/11543/4288)
- **Berkes, *Bazı Ankara Köyleri Üzerine Bir Araştırma* (1942; tesseract OCR), S4:**
  - Ev tipleri ve ahırın konumu ("evin birinci kısmını teşkil eden ahırın kapısı tamamiyle ayrı ve aşağıdadır"; "ambarlar ve ahırlar tamamiyle köyün içinde ve evlerin bitişiğindedir").
  - Servet sınıflamasında öküz, inek, manda, ahır ve samanlık.
  - Cinsiyete göre hayvan bakımı ("büyük hayvanlara erkekler, davara kadınlar bakarlar; süt sağmak kadınlara aittir"; kadınlar tezek yapar).
  - Sütçülüğün köyü dışarıdan arpa ve saman almaya mecbur bırakması; öküz alamadığı için ekin ekemeyen Keziban örneği.

  [11543/936](https://acikerisim.tbmm.gov.tr/handle/11543/936)

## 6. *Beyoğlu* (Fransızca gazete, İstanbul, 1939–1944)

Toplam 140 kayıt; tam liste `beyoglu_fransizca_isabetler.csv` dosyasında. Öne çıkanlar:

- **S0 × S1 (1942):** Millî Korunma kararıyla 10 yaşından küçük çift öküzleri ve mandalar ile 8 yaşından küçük ineklerin satışının, ihracının ve kesiminin yasaklanması; ardından kuzu kesiminin de yasaklanması ("cheptel national").
- **S3 × S0 (1940):** Kars hayvan ihracatçıları birliği ile SSCB arasındaki sığır ihracı sözleşmesi; Suriye'nin güney vilayetleri pazarlarından daha az hayvan alması.
- **S2 (1941):** Rumeli'nin kaybından sonra İstanbul'un et için Anadolu'ya ve "özellikle doğu vilayetlerine" bağımlı hale gelmesi: "Günlerce süren deniz yolculuğunda bakımsız kalan sığır bize zayıflamış ulaşır… mera olmadığından ahırlarda kuru yemle beslenir." Yem kıtlığında besicilerin hayvanı pazara sürmesi; et fiyatları.
- **S2 × S4 (1939–41), İstanbul sütü:** Sütçülerin saman ve yem fiyatları gerekçesiyle zam istemesi (bir ineğin günlük tüketimi ve maliyeti hesaplanıyor); vilayet veterinerlerinin ahırlarda yaptığı sağlık muayeneleri; süt zehirlenmesi vakası.
- **S3 (1940):** İstanbul veteriner müdürlüğünün salgınlarla mücadele istatistikleri (şehir içinde 5.780, dışında 116.284 hayvan muayenesi); Karağaç mezbahasında hastalıklı hayvanlar.
- **S1 (1940):** Tarım Bakanı Muhlis Erkmen'in Karacabey Harası'nı ziyareti; Tarım Bakanlığı'nın köylülere yönelik mandıra ve hayvan bakımı kursları (Hatay dahil).

## 7. Göz taraması gereken kaynaklar (OCR yok veya kullanılamaz)

| Yayın | Yıllar | Kayıt | Neden |
|---|---|---|---|
| *Ziraat Vekâleti Mecmuası* | 1924–1925 | [11543/4092](https://acikerisim.tbmm.gov.tr/handle/11543/4092) (14 PDF, 1,46 GB) | Arap harfli. **S0–S4 için çekirdek kaynak; öncelikli göz taraması** |
| *Ayın Tarihi* | 1923–1929 | [11543/3935](https://acikerisim.tbmm.gov.tr/handle/11543/3935) | Arap harfli; OCR bozuk |
| *Askerî Tıbbî Baytarî Mecmuası* | 1923–1928 sayıları | IA / TBMM | Arap harfli kısım |
| *Asrî Çiftçi* | 1927 | [11543/4173](https://acikerisim.tbmm.gov.tr/handle/11543/4173) | Arap harfli |
| *Toprak* | 1925 | [11543/3976](https://acikerisim.tbmm.gov.tr/handle/11543/3976) | Arap harfli |
| Yerel gazeteler: *Diyarbekir* (1925), *Urfa* (1925), *Mamüretülaziz* (1925), *Malatya* (1924), *Niğde* (1926) vb. | 1924–1928 | TBMM Açık Erişim | Arap harfli; S3 için sınır illeri |
| Kalan 40 öncelikli Latin harfli kayıt | 1930–1950 | TBMM Açık Erişim | Tesseract OCR sürüyor (`scripts/tbmm_ocr.py`) |
