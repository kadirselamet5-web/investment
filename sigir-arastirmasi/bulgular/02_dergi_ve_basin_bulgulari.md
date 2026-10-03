# Dergiler, Resmî Yayınlar ve Basın (1923–1950): Tarama Bulguları — Tur 1

**Taranan derlemler:**

| Derlem | Kapsam | Yöntem | Sonuç dosyası |
|---|---|---|---|
| TBMM Kütüphanesi Açık Erişim | 1923–1950 tarihli 658 kayıt (dergi, gazete, resmî yayın). Bunların 168'inde kurumun OCR metni vardı | OCR metinleri indirilip tezaurus v1.0 ile 3.000 karakterlik parçalar halinde tarandı | `dergi_isabetleri.csv` |
| TBMM Açık Erişim, OCR'ı olmayan Latin harfli kayıtlar | 49 öncelikli kayıt (halkevi dergileri, yerel gazeteler, Berkes) | PDF'ler indirilip tesseract (Türkçe) ile OCR'landı. **Devam ediyor:** şu ana kadar Berkes, *Doğuş* (Kars), *Karacadağ* (Diyarbakır), *Erzurum* ve *Derme* (Malatya) bitti; *Eskişehir Halkevi* sürüyor | `dergi_isabetleri_ocr.csv` |
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
- **Makale listesi (Tur 2):** 1929–1937 ciltlerinden "başlık + Yazan/rütbe/Dr. satırı" deseniyle 204 aday makale çıkarıldı. 40'ının başlığında strand terimi var: `atbm_makale_listesi.csv`. 1934–1937 sayılarının kapaklarındaki İÇİNDEKİLER blokları `atbm_fihrist_ham.txt`'de. OCR gürültüsü yüzünden liste eksik ve kısmen hatalı; başlıklar kullanılmadan önce IA görüntüsünden doğrulanmalı. Öne çıkanlar:
  - Mehmet Azmi, "Tederrün ve etlerin sureti muayeneleri" (1933, sayı 114). Karaağaç Mezbahası'nda 1 Mayıs 1931 – 31 Mayıs 1932 arasında kesilen 22.669 yerli öküz, 2.072 yerli inek ve 115 ecnebi öküz ve inek istatistiği; "kaçak sığır eti" ve süt kontrolü.
  - Osman Zeki, "Umumi harpta İngiliz ordusunun istihdam ettiği muhtelif at ırkları" (1932, sayı 113).
  - A. Müfhat, "Fotozoometri" (1930): fotoğrafın ıslah ve teksir-i hayvanatta kullanımı.
  - Zootekni Enstitüsü toplantı tutanakları (1933, sayı 114): "Türkiye'de dalak epidemileri ve mücadelesi".
  - TBMM'de "veteriner" kelimesinin reddedilip "baytar"ın korunması haberi (1934, sayı 121; ilgili TBMM görüşmesi 18 Haziran 1934, bkz. rapor 01 §S3).
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
- ***Derme* (Malatya Halkevi, 1937–46; tesseract OCR, Tur 2)** ([11543/3966](https://acikerisim.tbmm.gov.tr/handle/11543/3966)):
  - **"Malatya sığırcılığı ne âlemde"** (sayı 5, 1937; PDF s. 7–10; yazar içindekilerde OCR bozuk: "… Malkoç"), **S0, S1, S3**.
    - İlde 57.295 erkek, 51.080 dişi, toplam 108.375 sığır; "aşağı yukarı 8 kişiye bir öküz" düşüyor, çift öküzü olmayan köylü hesabı yapılıyor.
    - "Muhtelif kanların karma karışık bir surette damızlıkta kullanılması" yüzünden renk ve yapı karmaşası; "bütün dünya gelişi güzel hayvan yetiştirmekten vaz geçmiştir".
    - Arapkir, Besni, Adıyaman, Kâhta ve Darende sığırları karşılaştırılıyor.
    - Şap "köylünün sabanını yüzüstü bırakan" bir afet. Bazı "görgüsüz fen adamları" şapa önem vermiyor. Şarbon ve yanıkara için aşı.
  - Malatya atçılığının ıslahı: yonca, zootekni merkezi, aygır muayenesi (sayı 4, 1937; s. 11–12), **S1**.
  - Köy çocuğunun eğitimi: "öküzleri sulamak, hayvan yemlemek ve altlarındaki gübreleri temizlemek" (sayı 8, 1938; s. 21, 24), **S4** (ahır emeği).
  - Halk inanışları: ilk süt sağımına giden kadınların soğan dikmesi, koç katımında koçun üstüne kız çocuğu bindirilmesi (sayı 11, 1939; s. 23), **S1 ve S4** (üremeye ilişkin halk pratiği).
  - Sivas–Malatya yolundaki bir köyün tasviri: "duman ve tezek kokuları" klişesine karşı yeni köy (sayı 18, 1946; s. 19), **S4**.
- ***Erzurum* (Halkevi kültür dergisi, 1944–46; tesseract OCR, Tur 2)** ([11543/4274](https://acikerisim.tbmm.gov.tr/handle/11543/4274)):
  - **"Yakacak sıkıntısı"** (sayı 2, 1944; s. 18): Erzurum'da köylü ve şehirli halk kış boyunca "hayvan gübrelerini harcayarak tezek yakıyor". Gözler tezek dumanından kanlanıyor, gübresiz kalan tarlalar zayıf ürün veriyor. **S4 ve S2** (tezek, yakacak ve gübre çatışması).
  - Halk şiiri "Güz destanı": kışlık erzak listesi (tezek, peynir, yağ) ve "ahırda hayvan beslemek" (sayı 8–9, 1946; s. 31), **S4**.
  - Erzurum ağzı sözlüğü: "celep davarı", "çobannıh" vb. (sayı 11, 1946; s. 16), **S0**.
  - Mikroplar üzerine halk sağlığı yazısı: sığır vebası ve şap (sayı 6, 1945; s. 17–19), **S3**.
- ***Burdur Halkevi Dergisi* (1941), S4:** Köy odası şiiri: "Sağında bir ahır, solda samanlık" ([11543/3939](https://acikerisim.tbmm.gov.tr/handle/11543/3939)).
- ***Uludağ* (Bursa Halkevi):** Merinos koyunculuğu ve Karacabey (1935); Karacabey sel felaketi (1940).

### 3a. Halkevi dergileri, ikinci tur (*Eskişehir Halkevi Mecmuası* 1941–46, *Çorumlu* 1938–46, *Erciyes* 1938–45, *Görüşler* 1939–45): TBMM Açık Erişim OCR, Ekim 2026

- **S1 × S3, Eskişehir Vilâyeti Veteriner Müdürlüğü raporu (1944, sayı 78–80, s. 11–13):**
  - **Hayvan sayımı (1926 → 1944):** sığır 59.708 → 52.176 (1943'te 84.070). Manda 7.990 → 5.225. At 8.316 → 30.677. Savaş yıllarında ("fevkalâde vaziyetler") koyunda ve "pek az olarak" sığırda düşüş var.
  - **Teşkilatın iki ekseni:** "hayvanların ıslahı" ve "salgın hayvan hastalıklarıyla mücadele".
  - **Sığırcılık:** vilâyetin sığırları "büyük bir ekseriyetle **boz ırka** mensup, az bir kısmı ise yerli kara sığırlarından". Her yıl **Çifteler Harası'ndan boz ırk boğası** ucuz fiyatla alınıp köylere dağıtılıyor: "Şimdiye kadar vilâyetimizde **73 köye 114 boğa** verilmiş". Haranın damızlık inek kadrosu artırılacak.
  - **Eneme (iğdiş):** "köylüye bedeli mukabilinde verilen damızlık boğalardan lâyıkıyla istifade için" önümüzdeki sonbaharda "damızlığa elverişli olmayan bilumum aygır, tay, boğa ve **boğalık evsafını taşımayan danalar** enemeye tabi tutulacaklardır". Ziraat Vekâleti'nin gönderdiği ve vilâyetin kendi veteriner ve sağlık memurlarından **on ekip** kurulacak. Trakya, Muğla ve Bursa'daki iğdişin 1944'te vilâyet çapında **toplu bir kampanyaya** dönüştüğünü gösteriyor (rapor 04, 06).
  - **Atçılık:** il özel idaresi ve köy bütçeleriyle 20 aşım durağı. Aygır ve sıfat istatistikleri: 1939'da 97 aygır ve 3.676 kısrak, 1943'te 188 aygır ve 4.422 kısrak.
  - **Sergiler:** Mahmudiye'de at, sığır ve keçi sergisi (2.000 lira ikramiye), ayrıca Kaymaz, Beylikahır ve Seyitgazi'de sergiler. "Sergiler ayrıca mektep vazifesini görmektedir."
  - Rapor, Çifteler Harası'nın çevresindeki köylerin ıslahın merkez–çevre ilişkisini izlemek için seçkin bir yer olduğunu gösteriyor. Eskişehir, Trakya ve Muğla'dan sonra **üçüncü vaka adayı**.
- **S2, "Yoncanın memleket ziraatindeki büyük değeri"** (yüksek ziraat mühendisinin konferans özeti; sayı 51, 1941): yonca bir "at yemi" (Farsça *esbist*) olarak tanıtılıyor, yem ve gübre döngüsü anlatılıyor. 1945 tarihli bir yazıda (sayı 85) köylünün "bahçeye, hayvana, ineğe heves"i ve yonca ve korunga ekimi.
- **S0 × S1, "Çifteler çevresi köylü işletmeleri"** (1946, sayı 93–96): çiftçi aileleri üzerine işletme etüdü (irad hayvanları, ekim alanları, öküz). Ayrıca okunacak.
- **S3, "Veterinerimiz söylüyor"** (Ahsen Adaoğlu, 1943, sayı 63–64): et yoluyla insana geçen paraziter hastalık (kist hidatik). *Son Posta*'daki "Veteriner diyor ki" dizisiyle (1938–39) aynı tür.
- ***Çorumlu*** (1940): "büyük bir ziraat istasyonu veya devlet çiftliği tesisi zaruridir"; 1939 sayısında Osmanlı ağıl resmi (*resm-i ağıl*) ve âdet-i ağnam üzerine tarih yazıları (S0 ve S2'nin vergi arka planı).

- **S4, *Çorumlu*, "Köy etüdleri: Sarımbey" (Y. Z. Mühendisi Enver Ertüzün, Mayıs 1944, s. 1379 vd.):** "Hemen hemen bütün evlerin ahır ve ağılları avlu içinde, **insanla hayvan aynı kapıdan girip çıkıyor**. Bundan dolayı evlerdeki her temizliği bir pislik kovalıyor." Sokaklarda biriktirilmiş gübre, "idrarlı ve kokulu pis sular". Köyün kökeni Kuyumcu aşiretinin iskânına dayanıyor (deve ve koyun, Eğerci dağında yayla). 140 hane, 900 nüfus. 1924 duvarı normunun ziraat mühendisi gözüyle 20 yıl sonraki denetimi.
- **S2 × S4, *Çorumlu*, orman tahribi yazısı (1944, sayı 46, s. 1382):** Çorum'un evleri ve "kanatlı kapuları bu ormanı yiyerek kurulmuştur". Sobasız uzun kışlar yüzünden köylüler "odunsuzluk yüzünden **tarlaya dökecekleri gübreyi sulandırarak** çoluk çocuk **tezek çamuru** yoğuruyor". Ormansızlaşma, tezek ve gübresiz tarla zinciri (Erzurum 1944 ve Okaygün 1937 tanıklıklarıyla birlikte, rapor 06).
- **S2, *Erciyes* (Kayseri Halkevi), Kadir Gözübüyük, "Ziraat köşesi: Kayseride hayvan yemleri ve istifade imkânları" (1945, sayı 25):** "Hayvan yemi denince neden acaba ilk aklımıza gelen şey samandır?… Samanda sevilecek hiçbir şeyin olmadığını göstermektedir. O, safi sellülozdur… yüzde yarım… proteinli madde." Hayvanlar "karınları doymuş görünsün diye işkembelerini tıka basa samanla dolduruyor". Arpa ziraat hayvanına değil şehirdeki "payton arabası atlarına" gidiyor: "ziraat hayvanı işliyor, araba atları dişliyor". Yem çeşitleri listesi (burçak, fiğ, yonca, pancar, korunga, üçgül, yem turşusu). "Hayvansız ziraata sömürgecilik, ziraatsız hayvancılığa da arabacılık demek lâzımdır." **S2'nin saman merkezli kış yemlemesi eleştirisinin yerel uzman ağzından en açık ifadesi.**
- ***Erciyes*, "Hayvancılık ve hayvancılığın askerî, iktisadî, ziraî, sıhhî cepheden tetkiki ile baytarlığın rolü"** (1938, sayı 1–2, iki bölüm; zootekni otoritesi olarak "Profesör Krenhar"a atıf): 93 Harbi'nde dışarıdan at alma zorunluluğu; "istibdat idaresinde ölen hayvancılığımız"; baytarlığın halk sağlığını koruma rolü (şarbon, veba, serum). Yazarı OCR'da okunmuyor, PDF'ten bakılacak.
- ***Görüşler*** (Adana Halkevi, 1939–45): çiftliklerin ortakçılıkla işletilmesi ve öküz paylaşımı; Mansurlu'nun iktisadî durumu (aşiret, ahır, gübre). Ayrıca okunacak.

- **S4 × S1, *Akpınar* (Niğde Halkevi), M. Z. Oral'ın köy anketi formu (1935, sayı 11, s. 3–5):** Halkevi, köylerle ilgili yurttaşlardan ve muhtarlardan doldurmalarını istediği bir soru listesi yayımlıyor. **Coğrafya** bölümünde: "Köy evi kaç odalıdır. Mutfak, ambar, kiler (kayıt damı) vs. **ekleri, ahır; ahırlarla evin münasebetleri ve sebepleri**" ve "Mümkünse bir **ev planı**". **Temizlik** bölümünde: "Sokak ortalarına atılmış **gübre yığınları**, açık helâlar… karşı ilgi derecesi". **Köyün hayvanları** bölümünde: büyük ve küçükbaş sayıları, "cins ve ırkları"; yaşa göre adlar (düve, tosun, öveç); çift hayvanının çalıştırılmaya başlandığı yaş; günlük süt (kilo) ve et verimi; kaç yılda bir yavru; bakım, tımar ve sulama; hastalıkların köydeki adları ve köydeki tedavi yolları; "**Köylünün hayvanatı ıslah düşünceleri** ve bu hususta bilgileri var mıdır". **Ahır ile ev ilişkisi bir bilgi nesnesi olarak soru formuna giriyor:** devletin ve halkevinin köyü "tanıma" aracı. Formun cevapları sonraki sayılarda yayımlanmış olabilir; *Akpınar*'ın 1935–1940 köy monografileri ayrıca okunacak.
- ***Akpınar*** (1935–40) ve ***Erciyes*** (1946–47): yayla ve oba göçü (Akpınar 1936), köy monografileri (Erciyes 1946–47: pulluk, çayır, öküz; ısınmada odun ve az miktarda tezek), Kayseri ağzı sözlüğü ("hayvanlar için öğütülmüş un"). Ayrıca okunacak.

- **S4 × S2, *Gediz* (Manisa Halkevi), Manisa ovasının iktisadî coğrafyası (1946, sayı 90, s. 9–11; yazar başlıkta Kâzım Özses olabilir, doğrulanacak):**
  - **Hayvan sayısı (vilâyet / Manisa kazası):** sığır 175.668, koyun 499.225, keçi 809.534. Çift hayvanı olarak kullanılanlar: öküz 40.008 / 72.700, manda 4.558. Taşıma: 220 dört tekerlekli öküz arabası.
  - **Barınma:** "Koyun ve keçi… akşamları ağaç çitlerle yapılmış **ağıllarda** toplanırlar. **Sığır ve mandalar** da sürüler halinde yakın yayılımlara götürülüp getirilirler. **Fakat bunlar ağıllarda değil, her evde bulunan ve dam denen kapalı yerlerde kalırlar. Yaz kış bu böyledir.**" Beygirler şehirde ve ova köylerinde "ahır denen yerlerde" saman, arpa ve yulafla besleniyor.
  - **Hayvan türüne göre barınma ayrımı:** küçükbaş köy dışında ağılda, büyükbaş evin "dam"ında, at ahırda. S4 için sığırın evle bütünleşik barınmasının Batı Anadolu'dan bir tanıklığı (Doğu Anadolu'nun "kış odası" ve Çorum'un "aynı kapı"sıyla karşılaştır).
  - Yunt dağında hayvanlar sahiplerine ait taş çevrili korularda başıboş dolaşıyor, "kementle tutulur". Koyunda Karaman ile Dağlıç birleştirilerek "Çandır" ırkı; Manisa'da aygır deposu.
  - Kaynak olarak "İhsan Abidin, Anadolu'da ziraat ve yetiştirme, s. 614" anılıyor. Bu, İhsan Abidin Akıncı'nın TOK'taki "Anadolu Ziraat ve Yetiştirme Vaziyeti" eseri; uzman ağında Akıncı'nın etkisinin yerel yazıya ulaştığını gösteriyor.
- ***Taşpınar*** (Afyon Halkevi, 1934–46): Osmanlı terekeleri ve narh defterlerinde *lahm-i bakar* (sığır eti) fiyatları (1936); yayla ve göç şiirleri (1941). Tarihsel arka plan için ayrıca okunacak.

### 3b. *On Dokuz Mayıs* (Samsun Halkevi Dergisi, 1935–1949): TBMM Açık Erişim OCR, Ekim 2026

Kaynak: https://acikerisim.tbmm.gov.tr/handle/11543/4304. Halkevi OCR taramasının bu turunda 189 yeni isabet çıktı, çoğu bu dergiden. Puanı yüksek sayfalar okundu. Karadeniz kıyı ovası (Bafra, Çarşamba, Terme) için iç Anadolu ve Doğu tanıklıklarına karşılık gelen bir **nemli ova, mısır-tütün ve manda** profili veriyor.

- **S4, Dr. Kâmil Kunter, "Köy Evleri" (1941, İkincikânun–Şubat sayısı, s. 28–29; PDF s. 16–17):**
  - Sağlık gözüyle bir köy evi eleştirisi. İlk madde: "Umumiyetle **hayvanlarının ahırları barındıkları evlerin ve odaların altındadır.** Bunu… sıhhi bir hale koymak için mümkün olabildiği derecede **evlerinin altından ahırları çıkartıp evlerinin yanlarında veya karşı taraflarında yaptırılması** sıhhatlerince muvafık ve münasiptir."
  - Pencereler "otuz santim kutrunda birer delik"; "Her zaman hava mahsur kaldığı gibi **altından ahır kokusu da inzimam etmektedir.**"
  - Ahır için öneriler: "Ahırlarda **hayvanı bütün gübreleri içerisinde yatırdıklarından**… bu ahırların toprak kısmı kaldırım olmalı; ve hayvanı soğuktan korumak için üzerine kuru ot veya saman dökmelidir." Ahırın içi görülecek bir pencere olmalı.
  - Ayak yolu yatılan odanın yanında; hamamcık, kerevet yok.
  - **S4 için:** Karadeniz'de sığırın evin **alt katında** barınması (Gediz'deki "dam", Çorum'daki "aynı kapı" ve Doğu'nun "kış odası" ile karşılaştır). Hekimin önerisi 1924 Köy Kanunu'nun ev-ahır ayırma ilkesini tekrarlıyor; öneri yatay ayırma, yani ahırı yana ya da karşıya taşımak. Ahırın gübresi aynı metinde hem bir hijyen sorunu hem de yataklık meselesi olarak görünüyor.
- **S1 × S2, Mümtaz Ünal (Veteriner Müdürü), "Samsunun iktisadi varlıkları" (1942, sayı 59, PDF s. 6):** Samsun'u "Türkiye'nin Mezopotamyası" diye tanıtıyor. Hayvancılık faslı Osmanlı haralarına (III. Selim döneminde 135) ve Çarşamba ile Lâdik'te soysuzlaşmış "Canik atları"na dayanıyor. Bölgenin veteriner müdürü yerel ıslah anlatısını at üzerinden kuruyor.
- **S2, Mithat Çetiner, "Samsun'un hayvan durumuna toplu bir bakış" (1946, sayı 73, PDF s. 15):**
  - Üç kuşak: Bafra, Çarşamba ve Terme'nin mısır-tütün ovası, yukarı tütün kuşağı ve Havza-Lâdik.
  - Ovada mevcut yemle beslenen başlıca hayvanlar sığır ve manda.
  - Yem rejimi tarım ürününe (mısır) bağlanıyor.
- **S1, Samsun'da kurulması planlanan devlet çiftliğinin programı (1944, sayı 68, PDF s. 4):**
  - Köylüye **koşum öküzü** sağlamak; öküz yerine at koşumunu yaymak.
  - "**Mıntaka kara sığırlarımız bilhassa dejenere olmuş, süt verim kabiliyetleri pek azalmış**"; sade yağ başka illerden getiriliyor.
  - Domuz, kümes ve mandıracılık (krema makinesi: OCR'da "ekremüz" [?], yayık) öğretimi.
  - Kongrenin (1938) "yerli ırk soysuzlaştı" teşhisinin taşrada altı yıl sonra yerel bir kurum programına dönüştüğü görülüyor (S1 hipotez 4, rapor 05).
- **S3, şarbon ve mezbaha yazısı (1945, sayı 70, PDF s. 14–16; yazar OCR'da okunmuyor, PDF'ten bakılacak):**
  - "**Samsun bölgesi bu hastalığın en çok bulunduğu mıntakalardan biridir.**"
  - Leşlerin gömülmemesi yüzünden sporlar yayılmış; köylü şarbonlu tarlaya "**Mes'um tarla**" diyor ve oradaki merada hayvan otlatmıyor; hastalığın halk adı "**Dalak**".
  - Samsun Gazi caddesindeki köylü ayakkabısı yapan kunduracılar arasında şarbon sık görülüyor, ölenler var.
  - Önerilen tedbirler: ihbar; leşi açmadan, derisiyle 3 m derine gömmek ya da yakmak; yıllık aşı.
  - "Değerli bilginimiz ve profesörümüz **Süreya Aygün**" Pastör'ün şarbon aşısını "epiyi tadil etmiş", aşı yurtta bolca yapılıyor ve dışarıya da gidiyor. Bu, Aygün'ün şarbon aşısının taşra veteriner yazısında anıldığını gösteriyor (uzman ağı, `aygun`).
  - Mezbaha belediyenin "varidat menbaı" değil "sıhhat müessesesi" olmalı; fazla resim eti fakire pahalılaştırıyor.
  - Et buhranında Sivas, Kayseri ve Kars'tan getirilen kasaplık sığırlarda **silâhsız tenya** ("abdest bozan").
  - **S3 için:** halk bilgisi (mes'um tarla, dalak) ile laboratuvar aşısı aynı metinde. Sığır ticaretinin (doğudan sevk) parazit taşıdığı anlatılıyor.
- **S2, Çarşamba ilçe monografisi (1949, sayı 103, PDF s. 12):**
  - Çarşamba ovasında "zengin çayır ve otlaklar"; ova Caniğin koyun sürülerine kışlak.
  - "Ovanın geniş ormanlarında başı boş dolaşan ve **yılgı** denilen at sürüleri ile mandalar". Bu yarı yabani sürü düzeni Gediz'deki Yunt dağı korularıyla karşılaştırılmalı.
  - Sayılar: öküz 15.000, inek 17.000, manda 5.000, at 3.000; koyun yalnız 3.000.
  - Ürün: yılda 200.000 kg yağ, 1.000.000 kg yoğurt, 50.000 kg peynir. Çarşamba ve Terme ilçeleri hayvan ürünlerinde başta.

### 3c. *Kaynak* (Balıkesir Halkevi, 1933–1946), *İnan* (Trabzon Halkevi, 1938–1947), *Türk Akdeniz* (Antalya Halkevi, 1937–1939) ve *Ülker* (Niksar, 1936): TBMM Açık Erişim OCR, Ekim 2026

Kaynak: https://acikerisim.tbmm.gov.tr/handle/11543/4306 (*Kaynak*), …/11543/4309 (*İnan*), …/11543/4313 (*Türk Akdeniz*), …/11543/4299 (*Ülker*). Bu turda 309 yeni isabet çıktı. Puanı ≥6 olan sayfaların hepsi ve puanı 4–5 olup sığır, ahır, tezek, yem, mera ya da veteriner terimi taşıyan sayfalar (toplam 93) okundu. Balıkesir dergisi S4 için şimdiye kadarki en zengin halkevi kaynağı: köy yapısı, ateş inançları ve yerel söz derlemeleri aynı dergide il veteriner müdürünün raporlarıyla yan yana.

**Balıkesir (*Kaynak*)**

- **S4, A. Osman Balkır, "Balıkesir Köylerinde Yapı İşleri" (Ağustos 1935 ve devamı; PDF ttk_0235_1935_0031 s. 8–9, 0032 s. 12–13):**
  - Ahırın öbür adı "**hayvan-öküz damı**". Penceresiz ve alçak kapılı; ışık yalnız 50–60 cm'lik "**gübre deliği**"nden giriyor, "Burası da ışık için değil, hayvanların ahırda biriken gübrelerini dışa atmak içindir."
  - "Köylü, **hayvan damına yatıp kalktığı odasından daha çok özenir.** Kendi odasını süpürüp temizlemeden ahırını temizler."
  - Ev tek katlıysa ahır ve samanlık bitişikte, iki katlıysa birinci katta: "**Yani ahır ve samanlık asıl yapıdan ayrı değildir.**" Devamında: "birinci katlar genellikle hayvan ahırıdır. Aşağıda hayvanlar oturur, üstünde eviyesi."
  - Avlu kapısı ("koca kapı") sap yüklü bir öküz arabası geçecek kadar geniş.
  - Dış sıva "**Manda, Öküz pisliği veya At ve Merkep gübresi (fışkı) ile karıştırılmış çamurla**" yapılıyor: gübre bir yapı malzemesi.
  - Saman tepme imecesi; yapının temeli atılırken dana, koyun, kuzu ya da horoz kesilmesi.
- **S4, "Köylerimiz ve köycülüğümüz" (1935; ttk_0235_1935_0030 s. 12; yazar okunmuyor):** dağ köylerinde iki katlı evde "Alt kat hemen umumiyetle ahır ve samanlıkdır. **Ahırın gübre neşriyatı odaya siner ve bu pis neşriyat sıcak tutar itibarile hoşda görülür.**" Helâ yok; gübrelikler ve ahır kenarı kullanılıyor. Bu, ahır ısısının **köylünün gözünden olumlu** karşılandığını reformcu dilin içinden kaydeden ender bir tanıklık.
- **S3 × S0, A. Osman Balkır, "Balıkesir Köylerinde Ateş Üzerinde İnanmalar" (İlkteşrin 1935 ve sonraki sayı; ttk_0235_1935_0033 s. 15–16, 0034 s. 12):**
  - "**Kara yanık**" "yalnız sığır hayvanlarına gelen bir hastalık"; iyi edilmesinde "ateşin büyüsel gücünden yardım beklenir."
  - Köy sınırında, dağ eteğinde bir hayvan geçecek kadar tünel kazılıyor. Köy kâhyası akşamdan "Yarın büyük ateş yakılacak, evlerin hiç birinde ateş kalmıyacak" diye bildiriyor; bütün ocaklar söndürülüyor.
  - Adları köyde başkasında olmayan iki çıplak kişi fındık dallarını sürterek, kibritsiz ateş çıkarıyor. "Köyün **bütün sığırları sahipleri ile birlikte ateşin tünelden geçer**"; alevli odunlar hayvanlara, bazen sahiplerine değdiriliyor.
  - Avrupa'daki "need-fire" (Notfeuer) ritüeliyle birebir koşut [karşılaştırma bizim].
  - **Aynı sayıda** (s. 32–33) il baytar müdürlüğü 71.942 baş hayvana antraks aşısı yapıldığını ve 15 köyde şarbonla mücadeleyi bildiriyor. Halk sağaltımı ile devlet aşısı aynı dergide yan yana: S3'ün "iki bilgi rejimi" teması için doğrudan kanıt.
  - İkinci bölüm (0034 s. 12): tezek "fırın kızdırmak ve yemek pişirmek içindir", odun ve kömür oda ısıtır; "Sivri sinekleri yok etmek için de tezekle tütsü yapılmaktadır"; kül gübre yığınına, oradan tarlaya gider (S4).
- **S1 × S3, Baytar Müdürü B. Tunçay'ın raporları (1935; ttk_0235_1935_0028 s. 24, 0033 s. 32):**
  - 1933'te 5 köyde şarbon, 56 köyde şap (15.659 hayvan parasız ilaçla tedavi), 771 sığıra dalak aşısı.
  - 882 tosun ve 8 boğa enenmiş; 118 boğaya "muvakkat damızlık vesikası". 12 yılda 255 köy için 265 tipik boğa; 1.057 at, boğa ve tosun enenmiş.
  - "Vilâyetimiz **boz ırk mıntakası** olarak tayin ve kabul edildiğinden" Balya boz ırkı, **Bulgaristan'ın Plevne vilâyetinden getirilen** damızlık boğalarla ıslah ediliyor.
  - **Ağıllar Kanunu tatbikatı:** 42 ağıl yeniden yapılmış, 237 ağıl kanuna uygun ıslah edilmiş. 1929 kanununun taşrada uygulandığına dair sayısal kayıt (Gaste'deki "ağıl kanunu" doğrulamasıyla birleştirilmeli).
  - Tunçay ayrıca sütten kesme (dana iki aylıkta) ve "Hayvanlarda verem" yazıları yazmış: mütederrin ineğin sütü "katiyen" içilmemeli, 90–100 dereceye ısıtılmalı.
- **S3, Balıkesir belediye mezbahası (1933; ttk_0235_1933_0008_0009 s. 13):** on yılda 16.463 sığır, 3.064 dana, 3.149 manda kesilmiş; tüberküloz nedeniyle 49 sığır imha; 400 hayvana tüberkülin.
- **S1 × S2, Vet. Hekim Hasan Âli Türker, "Yurdumuzda Sığırcılık" (1946; ttk_0235_1946_0157 s. 6):**
  - Yerli ırklar: Kara, Boz, Doğu Kırmızısı, Güney Anadolu, Kilis, Çukurova, Dörtyol. Kara ve Boz "bakımsızlık" yüzünden günde 3–4 kg süt veriyor.
  - "Bu gün elinde bir iki sağılır ineği olmayan köylümüzün evi, **suyu kesilmiş bir çeşmeden farksızdır.**"
  - **Balıkesir İli Sığır Yetiştirme Birliği** (özel idare, belediyeler ve köy sandıkları ortaklığı) ve beş yıllık program: Balya ve Gönen'de boz ırk, Manyas'ta **Montafon** boğa üretme durakları; Susurluk-Demirkapı boz ırk boğa istasyonu güçlendirilecek. Boğalar dokuz ay köyde, kışın durakta bakılacak.
  - Savaş yıllarında dişi sığır ve mandaların kesimi "son günlere kadar yasak edilmiştir".
  - Şarbon "adeta bir **mera hastalığı**dır".
  - Aynı yazar "Merinosçuluğumuz" (1946) ile Karacabey Harası ve merinos çiftliğini de anlatıyor.
- **S4 × S2, Karacalar köyü (Savaştepe yöresi) monografisi (1946; ttk_0235_1946_0158–0161):**
  - Köy, Hardal aşiretinin birkaç obasının yurtlandırılmasıyla kurulmuş.
  - Varlık: 2.001 koyun, 300 inek, 60 öküz, 120 manda; bazı yıllar mandıra kuruluyor.
  - "**Hayvan ahırları çoğunlukla oturdukları evlerden ayrı yerlerdedir. Hanay evlerde hayvanlar alt odalarda yatarlar.**"
  - Gübre öküz damlarının yanına yığılıyor; "Sokaklar, her vakit gübrelerle kirli"; verem köyde salgın.
- **S2, "Kuraklığın Gelecek Seneye Zararları" (1945; ttk_0235_1945_0151 s. 5; yazar okunmuyor):**
  - "Yurdumuzda çiftçilik hayvan kuvvetine dayanır… Hayvanların kuvvetli ise ancak yem istihsaline dayanır… başta saman ve ot gelir."
  - "**Bu yıl kuraklık yüzünden ot ve saman çok kıttır.**" İlk tedbir çiftçiye yem dağıtmak.
  - "İlimizin iki yıl yağışlı gitse mutlak üçüncü sene kuraktır. **Sulamamız hiç yok.**" Çare: binalarda daha çok saman ve ot depolamak; aksi halde "hayvanlar iş görmez halde bahara çıkmaz."
- **S2 × S4, Karalar köyü gezisi (1937; ttk_0235_1937_0055 s. 9):** iki köy arasında "**mera ve sınır kavgası hiç bitip tükenmez**… Bir tutam ot için, bir karış toprak için yirmi yıllık bir ömrü feda etmek"; çamurlu, gübreli sokaklar; "Koyunların üzerinden atlayarak odamıza girdik."
- **Kültürel temsiller (S0):**
  - İbrahim Şevki Işıkman'ın şiirleri. "Kara Sığır" (1935, Kepsüt yolu): yaylımdan dönen sürü, "Çoğu düşmüş aç gibi bir kavram ot peşine". "Harmandan Dönüş" (1933): "Ocağının temelidir bir sapanla bir öküz!"
  - Halk şiiri "Kart öküz destanı" (1937): "Bu meralar senin inekler senin / Ömrün varı kadar yaşa kart öküz."
  - Yerel söz derlemesi (1933): "TEZEK — Hayvan tersinin yakılmak üzere kurudulmuşu"; "SIĞIRTMAÇ — Sığır çobanı".
  - Atasözleri: "Samanın varsa marta koy yoksa koca öküzün derisini arda koy" (S2, kış sonu yem darlığı).

**Trabzon (*İnan*)**

- **S1, Yahya Becan (Veteriner Müdürü), "Trabzon sığırcılığı üzerinde çalışmalar" (1946; ttk_0000_1946_0025 s. 13):**
  - 1946 sayımında il genelinde 148.544 inek, 3.015 öküz, 131.173 koyun: "inek sayısı en başta gelmektedir. **Bu vaziyet Trabzona mahsus bir durumdur.**" Yılda yaklaşık 90 milyon kg süt ve 20 milyon TL'lik yağ.
  - Trabzon doğudan gelen hayvanların "transit iskeleliğini" yaptığı için ırklar karışmış. Köylerde "**âdeta keçi gibi küçük**" ve günde yarım-bir kilo süt veren inekler var.
  - Islah "doğu kırmızısı veçhesinde" yürüyor: **Değirmendere Boğa Yetiştirme İstasyonu**; her köyde en az 50 inek için bir iyi boğa; kötü damızlıklar enenecek.
- **S1, Veteriner Fehmi Baysoy, "Trabzon Sığırlarının İnkişaf Yolları ve Verim Kabiliyetleri" (1947; ttk_0000_1947_0030 s. 6):**
  - Doğudan boğa getirme politikasını eleştiriyor: ıslah "esasen mıntıkamızda mevcut iyi cins ineklerin erkek yavruları" ile yapılmalı. Değirmendere istasyonu ve İnekhane 1946'da açıldı.
  - Süt verimi karşılaştırması: yerli kara 374 kg/202 gün; aynı ırk Devlet İktisadi İşletmeleri'nde ve **Çifteler Harası**'nda düzenli yemlemeyle 743 kg/227 gün; Batı Anadolu boz ırkı 650–800 kg; Doğu illeri 1.000 kg; Trabzon istasyon inekleri 1.100 kg.
  - "Trabzonlu da sığırını kasaplık için değil sütü için besler."
  - **S1 için:** Ankara merkezli "ithal boğa ile ıslah" çizgisine karşı yerel bir veterinerin "mahallî seleksiyon" savunusu. Aynı çatışma kongrede de vardı (rapor 05, S1 hipotezleri).
- **S3 × S4, Yahya Becan, "Tüberküloz Savaşı" (1947; ttk_0000_1947_0029 s. 6–7):**
  - "Bir çok yerlerde **sığır ahırlarında tavuklar da beslendiğinden** birinde olan hastalık kolayca diğerine de intikal edebilir."
  - "Trabzonda her nevi **yemek artıkları inek ve tavuklara verilmekte**" ve bu bulaşma yolu oluyor.
  - Trabzon 1944'te 56 milyon kg inek sütüyle Kars'tan sonra ikinci, ama "tahşiş edilmemiş iyi bir süt bulmanın imkânı yoktur."
  - Beşerî ve veteriner tababetin iş birliği çağrısı.
- **S4, Eyüb Sabri Lermioğlu, Karadağ yaylası gezisi (1944; ttk_0000_1944_0014_0015 s. 14):** "İnek, inek… **Köy kadınının evlât gibi sevdiği** munis hayvanlar… Çocuksuz ev bir virane ise, **ineksiz ahır bir faciadır** buralarda…" (kadın-inek bakım ilişkisi).
- **S2, M. Kemal Yanbeğ'in deyim derlemesi (1945; ttk_0000_1945_0018 s. 7):** "(Usul olmuş dana) kışın boyuna saman yiyen dişleri ezilmiş biçare yavru dana; ilk bahar gelmiş yeşile salıyorlar fakat usul olmuştur. Yeşil otları arzu ediyor fakat dişleri kamaşıyor yiyemiyor." Kış açlığının dile yerleşmiş bir izi.
- **S2, yonca yazısı (1945; ttk_0000_1945_0017 s. 21):** "bir kuru yonca onbeş kilo saman yerini tutar. Kuru yonca en iyi ve en kuvvetli bir kış yemidir."
- **S2 × S4, Kemal Kefeli ve İhsan Ural (Y. Z. Mühendisi), ekonomik yazılar (1947; ttk_0000_1947_0031 s. 4–5):** "Trabzon yağının bugünkü feci durumu". Köy aile bütçesinde iki sağılır inek (her biri 500 kg süt), hayvan yemi (arpa; mısır sapı bağı 15 kuruş) ve çiftlik gübresi.

**Antalya (*Türk Akdeniz*) ve Niksar (*Ülker*)**

- **S1 × S3, Veteriner Müdürü Ziya Uluer, "Veteriner İşleri" (1938; TTK_1938_0011_0012 s. 65–66):**
  - Cumhuriyetin ilk on yılında Balıkesir'den 70 kara sığır damızlık olarak taksitle dağıtılmış. Kara sığır cinsini bozacak 4.500 tosun ve dana enenmiş.
  - 17 numune köyü kurulmuş; buralardaki damızlık boğalar ihtiyar heyetlerince baktırılıyor.
  - "**Öküz kıranı** denilen hastalık tamamen ortadan kaldırılmış". Antraks aşısı veriliyor.
  - 1923–33: 223 köyde 118.449 baş hayvan, 19.009 hasta, 4.338 ölü.
  - Son beş yılda 10 **Montafon** boğası (Çirkinoba, Kemer, Kundu, Bozova); 165 köyde 3.416 ölü.
  - Dışarıya 157.638 baş hayvan (857.935 TL) satılmış; ihraç için **tahaffuzhane** yapılıyor.
- **Uzman ağı, "Antalya'nın yüksek tahsil mezunları" (1939; TTK_1939_0014 s. 15):** bir veterinerin meslek dökümü. Ad OCR'da sütun karışması yüzünden kesin değil; büyük olasılıkla **Kâmil Onat** (baba İbrahim Hakkı, 1305 İbradı doğumlu) [?, PDF'ten doğrulanacak].
  - 1335'e (1919) dek Konya Hayvanat Deposu Müdürü; 1335–40 Konya Veteriner Müfettişi; 1340–1927 Konya merkez sıhhiye veterineri.
  - **1927–28 Cebelibereket veba-yı bakarî mücadelesi grup reisi.**
  - 1929 Uzunyayla ıslah ve teksir-i hayvanat mıntıka müfettişi; 1931 Sultansuyu Harası müdürü; 1931 Cenup mıntıkası mücadele reisi.
  - 1938 Ziraat Vekâleti Veteriner İşleri U. M. idare ve müessesat şubesi müdürü, aynı yıl Adana Veteriner Başmüdürü.
- **S0 × S2, aşar destanı (1939; TTK_1939_0013 s. 13):** "Fükarada kalmadı koşmaya öküz… İltizamcı gelir, harman gezerek / Tohum öküz varmış sanki müşterek / Darı koymaz uşur yemlik diyerek."
- **S2, Niksar (*Ülker* 1936, ttk_0000_1936_0002–0003):** köylü "tarlalarına usulü dairesinde gübre vermemekte ve… hayvanlarına çok fena bakmaktadır"; ovada kışın binlerce hayvan kışlıyor; Bığırman yaylaları; panayıra köylüler "önünde boğası, elinde kovası" geliyor.

**Bu turun S4 tipolojisine katkısı (rapor 05):** Balıkesir aynı il içinde iki geometri veriyor:
- dağ köylerinde **alt kat ahır**: Balkır ve "Köylerimiz", "gübre neşriyatı… sıcak tutar itibarile hoşda görülür";
- ova köylerinde, Karacalar'da **evden ayrı ahır**, ama "hanay" evlerde yine alt oda.

Ahır ısısının köylünün gözünde bir değer olduğu ilk kez açıkça yazılı. Trabzon'da ise yemek artıklarıyla beslenen inek ve tavuğun **aynı ahırda** tutulması tüberküloz bulaşmasına bağlanıyor.

### 3d. *Ses* (Adana, 1938–1939), *Çorum* gazetesi (1946), *İnan* 1948, Ordu halkevi dergileri ve *Abant*: TBMM Açık Erişim OCR, Ekim 2026 (ikinci tur)

Kaynak: https://acikerisim.tbmm.gov.tr/handle/11543/4332 (*Ses*), …/11543/4192 (*Çorum*), …/11543/4309 (*İnan*), …/11543/4300 ve …/11543/4308 (Ordu), …/11543/3922 (*Abant*). Bu turda 99 yeni isabet çıktı; okuma eşiğini geçen 34 sayfa okundu.

- **S1, Halikarnas Balıkçısı, "Olağan İşler" (*Ses*, 1939, sayı 1; PDF 1029_1939_0001 s. 3 ve 20; "Şaka" köşesi):**
  - Bir hiciv. "Cenup Anadolusuna giden bir vali" arıcılık, tavukçuluk, narenciye ile "oranın yerli **sığır sıpasını** ıslah" etmeyi tasarlıyor.
  - Son model büyük arı kovanları kuraklıkta işe yaramıyor. Leghorn tavukları yerli tavuk kadar yumurtlamıyor ve avcı kuşlara yem oluyor; köylülere çifte dağıtılıyor.
  - Sığır için: "**büyük Kırım boğalarının getirtilmesi tensip edildi.** Bu boğalar yerli boğalar ve inekler gibi az buçuk yiyecekle doymuyorlardı. Köylüler onlara habire paspal, kepek, arpa taşımak mecburiyetinde kaldılar. Fakat iş burada bitmedi. **Küçük anadolu inekleri, ekspres lokomotifi gibi koskocaman Kırım boğalarına çektirilince, yükü kaldıramıyorlar, ve bel kemikleri kırılıyordu.**"
  - **S1 için:** kongreden bir yıl sonra ithal ırkla ıslaha yöneltilmiş edebî bir eleştiri. Uyumsuzluğun iki ekseni de var: yem (S2) ve beden ölçüsü (aşım ve doğum). Rapor 05 S1 hipotez 5 ("ıslahın darboğazı yem ve ahır") ile birebir örtüşüyor; Tankut'un 13 damızlık sığır anısının bir taşra karşılığı.
- **S1 × S3, Veteriner Müdürü Enver Can, "Cumhuriyette Gelişen Hayvancılık" (*Çorum*, Ekim 1946, sayı 1355–1364; PDF s. 9 ve 11–12):**
  - Hayvancılığın üç ayağı: "iyi vasıflı damızlıklar, rasyonel yemleme ve fenni barınaklar."
  - Cumhuriyet devrinde 5 hara, 7 aygır deposu, 4 inekhane, 4 sığır ıslah istasyonu, 1 merinos çiftliği, 2 numune ağılı kurulmuş. 1945'te haralarda damızlık sığır 1.342 baş.
  - "1945 yılına kadar fena vasıflı ve damızlığa elverişsiz (**1.333.029**) baş erkek hayvan enenmiştir." Enemenin ulusal ölçeği için şimdiye kadarki tek toplam rakam.
  - 1945'te Cenup ve Uzunyayla bölgelerinde 28.032 kısrağa 43.355 aşım. Hayvan varlığı "54 milyon". Pendik ve Etlik müesseseleri.
  - Aynı sayılardaki bir başka yazı (s. 7): köylünün hayvanları "ancak kara sapanı müşkilatla çekebilecek durumda", "her türlü zirai kalkınmayı evvela hayvan enerjisile yapmak zorundayız."
  - Enver Can 24 Kasım 1946'da İl Aygır Deposu'nda Ehli Hayvan Sergisi'ni açıyor (s. 23).
- **S3, *Çorum* gazetesinde "Çıkan ve söndürülen hayvan hastalığı" ilanları (1946; s. 4, 34, 37):** il daimi komisyonu her sayıda köy köy salgın listesi yayımlıyor.
  - Sungurlu, Keskin, Polatlı, Kırıkkale, Alaca ve Merzifon köylerinde sığır ve mandada şap ve antraks; Sulusaray'da yanıkara.
  - "**Orman Çiftliği sığırlarında antraks hastalığı çıktığı**", yani model kurumun kendi sürüsünde antraks.
  - Mezbahası olmayan yerlerde kesim resmi: dana 45, sığır 65, deve ve manda 100 kuruş (s. 17).
  - Bu ilanlar 1940'ların S3 coğrafyasını (salgın haritası) kurmak için **sistematik bir seri**. Diğer il gazetelerinde de aranmalı (G17'ye not).
- **S1 × S4, *İnan* 1948, "Veteriner Bahisleri" (ttk_0000_1948_0036 s. 3–4; yazar okunmuyor):**
  - 1947 mali sayımı: Trabzon'da 154.975 sığır, bunun 151.490'ı inek, yalnız 3.485'i öküz.
  - Kronacher'e atıfla "Her hayvan kendi toprağının mahsulüdür". Seleksiyon ve "Doğu kırmızı" ile ıslah önerisi; inekhane ve dana büyütme depolarıyla yılda 80–100 boğa.
  - "Burada bakım, besleme ve **hayvan meskenleri çok iptidai ve basittir.**" "Saldım çayıra, Mevlâ kayıra olmamalıdır." "Kışa zayıf ve mukavemetsiz giren hayvan ölüme mahkûmdur."
- **S2 × S4, Ordu Halkevi Mecmuası 1945, "Tarlalarımızın gübrelenmesinde yeşil gübre" (TTK_2115_1945_0006 s. 10):** sahil köylerinde "müsait mer'a ve çayır bulunmadığından fazla hayvan beslenememekte". Hayvanların çoğu da "yazın dört beş ay otlatılmak üzere yaylalara gönderildiğinden bunlardan pek az gübre alınabilmektedir." Kimyevi gübreye köylü "Avrupa gübresi" diyor. Yaylacılık ile ova gübresi arasındaki çatışma: S2 ve S4'ü (gübre) birbirine bağlıyor.
- **S3, Ordu Halkevi Mecmuası 1944, "Şarbon (Dalak)" (TTK_2115_1944_0005 s. 9):** halka yönelik anlatım. Hayvanlarda bulaşma "ekseriyetle otlarla"; yüzeysel gömülen leşin yerinde yetişen otları yiyen hayvanlar hastalanıyor ("şarbon evvelden beri çobanlarca da malumdur"). Samsun 1945'teki "mes'um tarla" ile aynı bilgi.
- **Kültürel temsiller (S0):** *Ses* 1938'de "Kasap" şiiri (imza OCR'da belirsiz): "Öküzler vapurdan çıkıyor. Öküzler salhaneye gidiyor… celep gülüyor… Öküzler, köfte olacaklar." İstanbul et arzının (deniz yoluyla gelen öküz) bir imgesi (S3 sevkiyat ile bağlantılı). *Ses* 1939'da köy romanı eleştirisinde "kara sabanı ve ihtiyar öküzü ile çorak toprağın bağrından bir avuç refah koparan" köylü tipi.
- Düşük ilgili: *Abant* (1945–47) anı ve gezi yazıları ("Vebai bakari zuhur etmiş"; Bolu'nun "geniş meraları yoktur"), *Yeşil Ordu* 1949 (yaylalarda ormanların koyun, keçi ve sığırla tahribi), Karaelmas 1938 (kelebek hastalığı).

### 3e. İl gazeteleri, 1947–1950 (*Çorum*, *Hür Millet*/Eskişehir, *Engizek*/Maraş, *Güney Postası*/Adana-Antep, *Dirlik*, *Hakikat*): TBMM Açık Erişim OCR, Ekim 2026 (üçüncü tur)

Kaynak: https://acikerisim.tbmm.gov.tr/handle/11543/4192 (*Çorum*), …/11543/4349 (*Hür Millet*), …/11543/4223 (*Engizek*), …/11543/4346 (*Güney Postası*), …/11543/4363 (*Dirlik*), …/11543/4195 (*Hakikat*). Bu turda 839 yeni isabet çıktı; okuma eşiğini geçen 294 sayfanın hepsi tarandı, yaklaşık 40'ı derin okundu. *Hakikat* 1950'nin OCR'ı çok bozuk, PDF'ten göz taraması gerekiyor. Bu gazeteler, rapor 06'daki büyük gazetelerin göremediği **1947–50 taşra** tablosunu veriyor.

**S2: 1948–49 kışı ve yem**
- **"Kasaplar haksız değildirler" (*Hür Millet*, Eskişehir, Şubat 1949):**
  - "Bütün iri ve ufak baş hayvanlar tamam **98 gündenberi ağıllarında kapalı durmakta, otlağa çıkamamakta**, arpa ve yulaf gibi pahalı yemlerle beslenmektedir."
  - Önerilen çare: "Toprak Mahsulleri Ofisinden sürü sahiplerine ucuz yem satmak, hatta ödünç vermek lâzımdır. Aksi takdirde… et buhranı iki misli artacak ve hayvan nesli mahvolmak…"
  - Ziraat Bankası Eskişehir şubesi kışın "tahminden çok şiddetli ve sürekli" olması üzerine çiftçiye 177.000 liralık yem yardımı yapmış, geçen yılın üç katı (*Hür Millet*, Nisan 1949).
- **"Köylerimizde Hayvancılık ve Otlaklar" (*Hür Millet*, Aralık 1949):**
  - Büyük şehirlerde bile "kasaplık hayvan kıtlığı" var. Birinci sebep: "Hayvanlar için ayrılmış olan **çayır ve otlakların tarla haline getirilmesinden otlaklarımızın azalması**."
  - Öbür sebepler: hastalıklar, kurak yıllarda yem eksikliği, ıslahsız "küçük cüsseli ve cılız" ırk, bakım bilgisizliği.
  - Öneri: yonca ve korunga ile köyde numune yoncalığı.
  - Rapor 05 S2 hipotez 2 (mera tarlaya feda ediliyor) için 1949 taşrasından doğrudan bir tanıklık.
- **Yem bilgisi (*Çorum*, 1950, "Tarım köşesi"):** "yalnız saman yedirilen bir hayvandan herhangi bir verim veya iş beklemek doğru değil"; saman "hayvanın karnını şişirerek" hazmı sağlar, "başka bir fayda temin etmez". Kesif yem, silo ("yem turşusu") ve yonca dizisi.
- **Mera kavgası ve Marshall:** *Çorum* 1950 Marshall planı ülkelerinin "meralar meselesi" toplantısını aktarıyor ("Meralara iyi bak, inekler kendi kendini…"); *Dirlik* 1949–50'de meraların geliştirilmesi. Eskişehir Ziraat Odası'nın bakana listesinde "mera davası" (Rıza Tarım, Eylül 1948): "Türkiyede hayvancılık ve hayvan üretme işi inhitat hâlindedir."
- **Kültürel izler:**
  - "Yem borusu" deyiminin açıklaması (*Güney Postası* 1948): Sarıkamış'ta aç atları yemsiz yem borusuyla oyalayan onbaşı.
  - Eskişehir'de bir hiciv şiiri (1949): "Aç yatarken ahırda benim kakavan öküz… Lâfla pilav pişerse deniz kadar yağ benden!"

**S1: boğa durakları ve ıslahın taşradaki ölçüsü**
- **İskilip Veterineri [Razi Akay], "Boğa Aşım Durakları ve Sonucu" (*Çorum*, 1949):**
  - İlde iki aşım ve bakım durağı var (merkez Bozboğa, İskilip Akkaya); üçüncüsü Alaca'da kuruluyor.
  - "Köylünün elindeki sığırlar vasatî **90–100 cm yükseklikte, 120–140 kilo ağırlığında**. Bir günde **1–1,5** [OCR "gr"] süt vermektedirler."
  - Islahla hedef 130–150 cm, 200–250 kg ve 10–15 kg süt; 150 liralık hayvan 200–250 lira edecek.
  - Duraklara yerel itiraz var: "bugün verimi yok diye bu yeni teşekkülü bozmak ve dağıtmak, eskiye rücu ile bu işi köylü eline bırakmak çok hatalı."
  - Köylünün sığırına dair şimdiye kadarki **en somut ölçüler**; kongrenin "soysuzlaşma" teşhisinin sayısal karşılığı.
- **Veteriner Umum Müdürlüğü Sığırcılık Şubesi Müdürü Nevzat Öner** (*Çorum*, 1950) İskilip ve Alaca duraklarını teftiş ediyor: merkezin sığır ıslahını il il izlediğini gösteriyor.
- *Çorum* il daimi komisyonu: Ağustos–Aralık 1948'de "Damızlığa yaramıyan **2298** erkek hayvan enenmiştir" (bkz. §3d'deki ulusal 1.333.029).
- **Eskişehir:** Çifteler Harası "senelerdenberi yüzlerce **boz ırk boğa**" dağıtmış (*Hür Millet*, Nisan 1948); hara 400–500 kg'lık "**Plevne ırkı boz inek**" satıyor (Haziran 1948).
  - Beylikahır hayvan sergisinde Montafon yavrulu inekler gösteriliyor (Ekim–Kasım 1949, Veteriner Başmüdürü Şevki Bey); Bozöyük'te boğa sergisi (Haziran 1949).
  - Çifteler'de "süt tayı tavlasının ağıla tahvili" ihalesi (Mayıs 1948): hara at yetiştirmeden koyun ve sığıra kayıyor.
- **Maraş (*Engizek*, 1949):** Veteriner müdürü B. Necmi Renda, Antalya Boztepe Devlet İnekhanesi'nden yedi baş "Güney sarı, kırmızı" boğa getirmeye gidiyor. Halk Bankası kumbara çekilişiyle de boğa ikramiyesi veriliyor. Belediye piyangosunun ikramiyeleri arasında "bir çift manda öküzü", "bir çift karasığır öküzü", "inek" var.

**S3: tüberküloz ve sığır**
- *Çorum*'da Veteriner Müdürü [Enver Can], "Verem Hayvandan İnsanlara Nasıl Bulaşır" (1948).
- İl veteriner teşkilatı 1949'da merkez, İskilip ve Sungurlu ile ikişer köyde **sığır ve mandalarda tüberküloz taraması** başlatıyor.
- Merkez Veterineri M. Nazım Okay, "Sığırlarda Tüberküloz" (1950).
- Aynı yıl bir tüccar 100 inek alacak "fenni bir ahırla bir fenni süt evi" kurmak için başvuruyor (1948).
- S3'te verem, 1940'ların sonunda insan verem savaşına (Verem Savaş Dernekleri) bağlanan yeni bir sığır sorunu olarak öne çıkıyor.

**S4 ve S0: ortak sürü, gübre, siyaset**
- **Engizek 1949, mizahi diyalog:**
  - Belediyenin "Çiftçi Mallarını Koruma" bekçileri bağ ve bostan kıyısında yakaladıkları hayvanları "tutsak pazarındaki deposuna" dolduruyor; ceza "D.P.liden beş, C.P.liden iki buçuk lira".
  - "Sabah sabah mallarını **nahırcıya** teslim edenler…"; başıboş hayvan cezasını "sığırtmacın aylığından" kesme önerisi.
  - Kasabada ortak sürü (nahır) düzeni ve 1946 sonrası çok partili siyaset aynı sahnede.
- **Kent içinde ahır ve gübre:** Nizip'te jandarma konağının altındaki ahırın gübresi her gün cadde kenarına yığılıyor (*Güney Postası*, 1947). Maraş'ta köylü tasvirinde "ahırların nemli tezeklerinden… havalanan kara sinekler" (*Engizek*, 1949).
- **Aşiret:** "mevcudu 10 binleri bulan Aydınlı aşireti" Engizek, Toros ve Binboğa yaylalarından iniyor; bir oba üyesi "göçüp konmaktan bıktıklarını" ve yerleştirilmeyi beklediklerini anlatıyor (*Engizek*, 1949).
- **Siyasal mecaz (*Engizek*, 1948, piyes):** "memleketimizi… bir **manda** yapmak istiyorlar… Güya biz süt veren bir inekten başka bir şey olmayacağız… Biz ise kuru ot yiyerek onları besleyeceğiz." Sağılan hayvan bir bağımlılık (manda/mandate) imgesi olarak kullanılıyor.
- **Canlı hayvan ihracı (*Hür Millet*, Eylül 1948):** Ticaret Bakanı Cemil Barlas'ın ihracat kararı İstanbul basınında "yaygara"ya yol açmış. Yazara göre ihraç "Erzurum için hayati bir iştir"; yasaklanırsa "kaçakçılık başlıyacakdır". S3 ve sınır ile et fiyatı çatışması.

### 3f. *Buç* (Kırklareli, 1935–36), *Çorum* 1947, *Türk Yolu* (İzmit, 1930–32), *Gazi Yolu* (Bursa, 1931–33), *Milli Ticaret*, *İstanbul Postası*, *Dirlik*: TBMM Açık Erişim OCR, Ekim 2026 (dördüncü tur)

Kaynak: https://acikerisim.tbmm.gov.tr/handle/11543/4221 (*Buç*), …/11543/4192 (*Çorum*), …/11543/4196 (*Türk Yolu*), …/11543/4224 (*Gazi Yolu*), …/11543/4318 (*Milli Ticaret*), …/11543/4366 (*İstanbul Postası*), …/11543/4363 (*Dirlik*), …/11543/4355 (*Serbest Cumhuriyet*). Bu turda 910 yeni isabet çıktı; eşiği geçen 349 sayfanın hepsi tarandı.
- *İleri Gazetesi* 1944'ün (139 sayfa) OCR'ı büyük ölçüde okunamaz durumda; seçilebilen içerik et fiyatı, mezbaha kesim sayısı ve hileli süt şikâyeti.

**S4 ve S2: Trakya'da tezek, gübre ve zorunlu yoncalık (*Buç*, Kırklareli Halkevi)**
- **Trakya Umumi Müfettişi General [Kâzım] Dirik ile söyleşi (1935; PDF 0186_1935_651-666 s. 38, 42):**
  - "Trakya için hayvancılık büyük zenginlik kaynaklarından biri. Buradan kaçanlar giderken yüzbinlerce koyun götürmüşler; götürülenler yerine yenileri beş-on yıl içinde yerden fışkırır gibi çoğalmış."
  - Beş yıllık plana göre her köy bir koruluk yapmaya mecbur. Gerekçe: "**Köylünün tezek kullanması gübresini toprağında kullanmaması demektir ki bu durum çiftçi için acı ve sıkıntılıdır.**"
  - **S4 için:** tezek ile gübre arasındaki çatışma, bir umumi müfettişin kalkınma planında yakıt politikasına (köy korusu) dönüşüyor. Rapor 05'teki "tezek ekonomisi" hipotezinin devlet tarafındaki karşılığı.
- **Trakya beş yıllık programı (1936; 0186_1936_668-714 s. 50):**
  - Yoncalık ve çayır tohumu (Kayseri ve Yeşilköy'e siparişler); "Ot ve çayır yetiştirmeye ve balya makineleriyle bunları toplamaya dikkat edilecek ve makineler kredi ile alınacaktır."
  - "Her köyün manevi şahsiyeti adına en az 5–15 dönüm ektirilmek ve bunları köy kurulunun mecburi ödevleri arasına aldırmak işleri bitmiş gibidir. **Bu köylerin sayısı binden aşağı değildir.**"
  - S2 için kongre öncesi (1936) bölgesel bir **zorunlu yem ekimi** rejimi.
- **Göçmen iskânı ve kış yemi (1936; s. 5):**
  - Göçmenlere hayvan ve pulluk verilmiş; ilkbahar için 10.000 pulluk daha alınıyor ve "ilkbaharda yeniden öküz" alınacak.
  - "Göçmenlerin büyük baş hayvanları için ilkbahara kadar geçindirecek ot ve saman alınmasının Sıhhiye Vekâletince kararlaştırılması" ile hayvanlar korunuyor. S2 ve S0 kesişimi: iskânın bir parçası olarak devletin sağladığı kış yemi.
- **Damızlık ve sayım (1936; s. 106, 110):**
  - Trakya'ya atlar Karacabey'den, boğalar "[yurt] dışından satın alınarak" getirilmiş; baytar olan yerlerde aşım durakları kuruluyor.
  - Kırklareli sayımı: Şubat 1936 su baskınına rağmen sığır 85.745'ten 89.847'ye, manda 9.543'ten 10.256'ya çıkmış.
- **Trakya ağılları (*İstanbul Postası*, 1939–40):** "(4700)'ü bulan sıhhi ağıllar"; bir buçuk milyon koyun; koyunculara 300.000 liralık avans. Rapor 02 §3c'deki Balıkesir Ağıllar Kanunu verisiyle birlikte okunmalı.

**S4 ve S2: Çorum köylerinde ahır (Nazım Okay, 1947)**
- **"Veteriner Öğütleri: Verim Üzerine Tesir Eden Bakım ve Yemleme" (*Çorum*, 15 Ocak 1947; yazan Nazım Okay, Merkez Veteriner Hekimi):**
  - "Temas ettiğim köylerdeki hayvan barınakları hiç de sıhhi değildir. **Ahırlar umumiyetle binanın zemin katını teşkil etmektedir.** Yaz ve kış rutubetini muhafaza eden duvarları, **kışın sıcak olsun diye zeminde bırakılan gübre** … durumunu bir kat daha güçleştirmektedir. Gübreden çıkan amonyak ve rutubet…"
  - "Kapalı ve ışık görmeyen barınaklardan çıkarılan hayvanlar evvela hareketsiz durmakta ve bilâhare sallantılı bir yürüyüşle… **bir müddet görmedikleri** tesbit edilmiştir."
  - "Yaz ve kış nasibini meradan almak mecburiyetinde kalan hayvanlarımız kışı büyük bir zafiyet ve dermansızlık içinde [geçiriyor]."
  - "**Köylümüz hayvanlarını feleğin kesesinden geçindirmeğe alışmış**… saman vermek dahi bir külfet ve fuzuli masraf olduğu ileri sürülmektedir. **Yemleme ancak ziraat hayvanlarına inhisar etmekte**."
  - **S4 için:** Balıkesir 1935'teki "sıcak tutar itibarile hoşda görülür" (§3c) Çorum 1947'de veteriner gözünden tekrar ediyor: gübre, ahır ısısı için bilerek bırakılıyor.
  - **S2 için:** yem yalnız koşum hayvanına veriliyor, öbürleri meraya bırakılıyor. Bu, kışlama krizinin (S2 H1) hane içindeki bir hiyerarşi olduğunu gösteriyor.
- **DDT ve ahır sayısı (*Dirlik*, 1948–49):** Sıtma Savaşı ilaçlamasında ilçede "520 ev, 1560 oda, 35 cami, **1200 ahır**, 670 samanlık ve 550 kümes"e DDT sıkılmış. Ev başına iki ahırdan fazla düşüyor; ahırlar sıtma savaşının da hedefi.

**S3: hastalıkta köy protokolü**
- **"Korunma çareleri" (*Türk Yolu*, İzmit, 1931):**
  - Bulaşıcı hastalıkta hayvan sahibi muhtara, muhtar hükümete haber verir. Hasta hayvan ahırdan çıkarılmaz, yemi ve suyu ahırda verilir.
  - "Baytar gelinceye kadar herkes sabahleyin **hayvanını sığırtmaca vermemeli**, ahırında beslemeli veyahut çocuğuyla ayrı bir mer'ada… otlatmalıdır." Ahırlara kireç dökülmeli; ölen hayvan derisi yüzülmeden derin bir hendeğe gömülmeli.
  - "Köyünüzde çıkan hastalığı hemen civar köylere bildiriniz ve **mer'asını derhal değiştiriniz**."
  - Karantinanın köy düzeyindeki aracı ortak sürüden (sığırtmaç) çekilmek. S3 ile S4'ü ortak sürü düzeni üzerinden bağlıyor.
- *Gazi Yolu* (Bursa, 1932), "Köylüye faydalı bilgiler: Dalak hastalığı": çobanlar hayvanın burnunu sıkıp "kan işerse dalak olduğunu anlarlar" (halk teşhisi).

**S1 ve S0**
- *Gazi Yolu* 1933: Alıcılar'daki hayvan sergisi, "Hayvan ırkının Bursa vilâyetinde ıslahına sarfedilen büyük emekler boşa gitmemiştir." Aynı sayfada "Beyaz Irk: Bugünkü Almanya'nın Dayandığı Kuvvet" (Rosenberg alıntısı). Hayvan ıslahı ile ırk söylemi aynı sayfada yan yana; S1 hipotezlerinde "ırk" kavramının çift kullanımı için not.
- *Serbest Cumhuriyet* (1930): Ziraat Vekâleti İnanlı, Karacabey, Çifteler ve Konya inekhaneleri için **205 inek** satın alıyor.
- *Milli Ticaret* (1930–33): İstanbul'un "süt meselesi". Çevrede "mebzul" temiz süt üretildiği halde şehir "mağşuş sütten başka bir şey bulamamaktadır"; süt işi bir ara bir şirkete verilmiş, sonuç alınamamış.

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

## 6a. *Türk Baytarlar Cemiyeti Mecmuası* (İstanbul, 1930–1933; İBB'de 8 sayı OCR'landı)

İlmî ve meslekî, gayrimuntazam yayımlanan bir dergi. Cemiyet 5 (veya 6) Şubat 1930'da, dergi 1 Teşrinievvel 1930'da kuruldu. Mesul müdürü İsmail Hakkı; heyeti idarede Mardin mebusu muallim Mehmet Nuri. İBB'deki sayılar: 1, 3, 4, 6, 7, 8, 9, 10 (toplam 585 sayfa; 157 sayfa puan ≥6). **Tarih uyarısı:** katalog ve kapakta 4. sayının tarihi "15 Nisan 1930" görünüyor. Oysa 1. sayı Ekim 1930'da çıktı ve bu sayı Şubat 1931'deki Birinci Ziraat Kongresi'nin encümen kararlarını yayımlıyor. Doğru tarih **15 Nisan 1931** olmalı.

- **S3, sığır vebası ve "usul-i basit"/"usul-i muhtelit" tartışması (sayı 4, 1931, s. 6–8; İsmail Hakkı, "Memleketimizde Sığır Vebası ve Baytarlık"):**
  - Sığır vebası "yarım asırdanberi" Rusya ve İran'dan doğu vilâyetlerine giriyor ve oradan bütün ülkeye yayılıyor.
  - Cemiyet heyeti idaresi durumu İktisat Vekili Mustafa Şeref'e arz etti. Vekil, sığır vebası ve "ıslahı hayvanat" usullerini belirleyecek bir **baytarî kongre** toplanmasını uygun buldu.
  - Eski Ziraat Vekili Sabri Bey'in Almanya'dan getirttiği salgın hastalıklar uzmanı **Hoffmeister**, raporunda yalnız serumla yapılan mücadelenin ("usul-i basit") yetersiz olduğunu yazdı. Hoffmeister, serumla birlikte virüslü kan zerkini ("usul-i muhtelit") önerdi.
  - Sabri Bey 1926'da baytarlarla bir ilmî içtima yaptırdı, ama burada "tarafgirlik ve hissiyat galebe çaldı". "Hocamız Doktor Refik Bey" ve başka baytarlar muhtelit usulü savunduğu halde usul kabul edilmedi, yalnız tecrübesine karar verildi.
  - Yazara göre sonuç: "Sığır Vebası bu sene de… memlekette baştanbaşa sirayet, yüz binlerce hayvan" telef.
  - S3'te dış sınırdan giren salgın ile meslek içi bilgi çatışmasının kesiştiği birincil tanıklık. TBMM tutanaklarındaki sığır vebası tartışmalarıyla karşılaştırılmalı (rapor 01).
- **S1 × S2 × S0, Birinci Ziraat Kongresi (Şubat 1931) 16. Encümen (hayvancılık) mazbatası (sayı 4, s. 36–46; mazbata muharriri Tevfik Süleyman, Karacabey Harası):**
  - Encümen reisi Mardin mebusu muallim Nuri Bey. Üyeler arasında Pendik Bakteriyoloji Enstitüsü müdürü Şefik, İktisat Vekâleti Zootekni şubesi müdürü Nureddin, sütçülük laboratuvarı şefi Ekrem, Yüksek Baytar Mektebi zootekni laboratuvarı şefi İsmail Hakkı, tavuk enstitüsü müdürü Kadri, sütçülük mütehassısı Servet, Karacabey Harası ziraat mütehassısı Kemal ve vilâyetlerden yetiştiriciler var.
  - Mazbatadaki tespitler: "İneklerimiz senede 300–600 kilo süt, 60–150 kilo et veriyorlar". "Son istatistikler memleketimizde 5 milyondan fazla sığır olduğunu göstermektedir". "Türkiye'de süt Avrupa'nın en pahalı memleketlerinden daha yüksek bir fiyatla satılır". Hayvanlar ve ürünleri dünya piyasasına arz edilmek zorunda.
  - Bu mazbata, 1938 FVADC Hayvan İşleri Komisyonu'nun yedi yıl önceki öncülü. Tam metni ayrıca okunup karşılaştırılmalı.
- **S1 × S2 × S4, Tevfik Süleyman (Karacabey Harası), "Yerli sığırlarımıza kıymet ve ehemmiyet verelim" (sayı 3, 30 Aralık 1930, s. 12 vd.):**
  - "Hollanda'nın senede 10 bin kilo süt veren ineklerini memleketimize getirip dağıtmak ve bunlardan aynı miktarda süt almak kabil değildir. Yetiştiricilerimizin kabiliyetleri, ziraat vaziyetimiz, **ahırlarımız, mera ve çayırlarımız** bu gibi yüksek hasılat veren hayvanları… yetiştirmeğe müsait değildir."
  - Yerli ırk "yalnız bakımsızlık, gıdasızlık yüzünden dejenere" olmuş. "İyi bir bakım, bol bir gıda, esaslı bir seleksiyonla" birinci derecede süt, sonra et ve koşum hayvanı olabilir.
  - **S1 için kilit metin:** ithal ırk ile yerli ırkın seleksiyonu tartışmasında, ahır (S4) ve yem/mera (S2) koşullarını ıslahın ön şartı sayan erken bir "yerli ırk" savunusu. Rapor 05'teki S1 hipotezine eklenmeli.
- **S3 × S4, Zeynelâbidin, "İstanbul Mezbahasında tederrün vekayii" (sayı 4, s. 76–78):**
  - Yabancı istatistiklerle (Park ve Krumwiede; Fransa) sığır kaynaklı insan tüberkülozunu tartışıyor.
  - İstanbul mezbahasında görevli bir meslektaşın koltuk altındaki lenf bezinde "bakarî menşeli" tüberküloz bulunmuş.
  - "Mezbaha memleket hayvanatının… bilhassa hastalıklarını gösteren aynadır." Sütün "ölüm nakili olmaktan" kurtarılması çağrısı.
  - Zoonoz ve çocuk sütü üzerinden S3'ü insan sağlığına bağlayan bir metin. *Son Posta*'daki "Veteriner diyor ki" dizisinin (1938–39) öncülü.
- **S3 ve uzmanlık ağı, taşra baytar kadrosu (sayı 4, 1931, s. 97, "Haberler"):**
  - Askere sevk edilecek 13 genç baytarın görev yerleri listelenmiş: Havza, Trabzon merkez, Balya, Maraş, Daday ve Ordu hükümet baytarları; Etlik Müessesesi bakteriyoloji asistanları (Cevdet Nuri, Selâhattin Azizi); Sivas ve Çifteler aygır deposu baytarları; Erzurum "mücadele baytarı"; Karacabey Harası asistan baytarı.
  - Bunların bir kısmı "vebayi bakari dolayısıyla memuriyeti asliyeleri başında bulunmayıp uzak şark vilâyetlerinde mücadelede" bulunuyor. Sığır vebası, taşra baytarlarını görev yerlerinden doğuya kaydırıyor.
  - Trabzon İdare-i Hususiyesi dört baytar istihdam ediyor (biri zootekni mütehassısı) ve 1931'de damızlık hayvan alımına 8.000 lira ayırmış.
- Ayrıca okunacak yazılar:
  - Hoffmeister, "Türkiye'de Baytarlık" (sayı 4).
  - "Sığır vebası ve bir mülakat" (İsmail Hakkı) ve "Veba-i bakar" (Mustafa Fehmi) (sayı 3).
  - "Basit mi? Muhtelit mi?" (Hüsamettin, sayı 3).
  - "Sun'i ilkah" ve "Beygir piroplazmozu" (sayı 4).
  - "Lüleburgaz hayvan sergisi" (sayı 1).
  - "Haranın tarihçesi (Karacabey Harası)" ve "Ziraat Vekâletinin bir tekzibi" (sayı 8).
  - "Konya Nümune Baytarlık kursları" (sayı 9).
  - Aza listesi (sayı 4): uzmanlık ağı için tam üye listesi.

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
