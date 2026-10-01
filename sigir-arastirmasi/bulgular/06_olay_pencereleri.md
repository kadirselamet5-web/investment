# Rapor 06: TBMM olay pencerelerinde gündelik basın (ara rapor)

## Kaynak ve yöntem

- **Pencereler:** `01_TBMM_tutanak_bulgulari.md`'deki sığırla ilgili 46 meclis olayının her biri için olaydan 7 gün önce ile 21 gün sonrası (`scripts/ibb_olay.py`, 1929–1943). Liste: `cumhuriyet.tsv.pencereler`.
- **Gazete:** önce *Cumhuriyet* (İBB Atatürk Kitaplığı). Bugüne kadar OCR'lanan pencereler:
  - SSCB baytarî mukavelesi (Şubat 1929);
  - Mandıra ve Ağıllar Kanunu (Mart 1929);
  - Umumi Hıfzıssıhha Kanunu (Nisan 1930);
  - Baytar Süreyya'nın sığır vebası aşısı sualı (Haziran 1932);
  - Yüksek Ziraat Enstitüsü kanunu (Haziran 1933);
  - Bulgaristan baytarî mukavelesi ve İskân Kanunu (Mayıs–Haziran 1934);
  - Hayvanlar Vergisi Kanunu (Ocak 1936, sürüyor).
- 1931 sayıları İBB'de eksik; 1940-06 penceresi boş çıktı.
- **Tarama:** `tara.py`, terim puanı. Puanı ≥8 olan sayfalar tek tek okundu.
- **Sınırlılık:** İlk gözlem şu: pencerelerdeki isabetlerin çoğu meclis olayının kendisini değil, aynı haftanın taşra haberlerini, mezbaha istatistiklerini ve canlı hayvan fiyat tablolarını veriyor. Meclis görüşmeleri *Cumhuriyet*'te çoğunlukla birkaç satırlık A.A. haberi olarak geçiyor.

## Öne çıkan haberler

| Tarih | Gazete, sayfa | Başlık / konu | Strand | Not |
|---|---|---|---|---|
| 1933-06-10 | *Cumhuriyet* 5 | **"At nesli ıslahı: Milâsta bir sıfat istasyonu tesisi isteniliyor"** (Milâs muhabiri Ahmet Nazmi) | **S1** | "Memleketin iktisadî ve ziraî yükünü taşıyan, vatan müdafaasında en çok işe yarıyan at ve öküz… cinsiyetinin bütün kudret ve kuvvetini kaybettiğini, boylarının alçaldığını, cüsselerinin küçüldüğünü, tenasüplerinin bozulduğunu" görmek yürek sızlatıyor. **Muğla vilâyet meclis-i umumisi** elindeki üç damızlık aygırı "lüzumsuz" bulup satmak istemiş, vali buna izin vermemiş. Çözüm: "mütehassısların raporlarına uygun… büyük bir seferberlik". Islahın yerel meclis bütçesiyle çatışmasını gösteren erken örnek |
| 1933-06-12 | *Cumhuriyet* 6 (Halk sütunu) | Halkalı Ziraat Mektebi son sınıf öğrencilerinin teşekkürü | S1 | Karacabey Harası'na tetkik gezisi. Hara müdürü Şefik ve "atçılık, koyunculuk, **kara sığır** ve ziraat şubeleri mütehassısları". Harada ayrı bir kara sığır şubesi olduğunu gösteriyor |
| 1934-05-10 | *Cumhuriyet* 6 | **"Uzunyayla ovalarında yetişen hayvanların ıslahı için hükümetin kurduğu teşkilât müspet neticeler veriyor"** (Kayseri) | S1, S2 | 1882–85'te Kafkasya'dan gelen atçı muhacirler. Her evde en az bir iki kısrak; 300–400 atlık "yılkı" sürüleri yaz boyunca açık çayırda, kışın Çukurova'ya götürülüyor (**mevsimlik göç ve kışlak**: S2). Sıfat (aşım) istasyonları, Kayseri baytar müdürü Dursun Fahrettin. Ziraat Vekâleti yulaf tohumluğu dağıtıyor |
| 1934-06-02 | *Cumhuriyet* 3 (Şehir işleri) | "Bir ayda kesilen hayvanlar" | S0, S1 | Karaağaç mezbahasında bir ayda 42.387 hayvan kesilmiş. Bunların içinde **1.860 öküz, 209 inek, 445 manda, 109 dana, 301 malak, 6 boğa** var. İstanbul'da kesilen sığırın büyük çoğunluğu **öküz**: çift hayvanı ömrünü tamamlayınca et piyasasına giriyor. Bu oran, 1942 Millî Korunma'daki çift öküzü kesim yasağının (rapor 02 §6) arka planı |
| 1936-01-16 | *Cumhuriyet* 3 (A.A.) | **"Muğla, 9 damızlık boğa aldı"** | **S1** | "İlimizde öküz soyunun düzeltilmesi için boz ırktan olmak üzere dokuz damızlık boğa satın alınmıştır." Dağıtım: merkeze 3, Milâs'a 1(?), Nümune köyüne 5 (OCR'da rakamlar bozuk). 1939'da Muğla'daki 34 Boz Plevne boğasının (rapor 04, *Haber* 1939-02-26) başlangıcı |

### İkinci parti (Kasım 1936 – Haziran 1937)

Pencereler: Emin Draman'ın muhacir ahır ve samanlıkları sorusu (Kasım 1936); Orman Kanunu (Ocak 1937); Ziraat Vekâleti teşkilat kanunu (Mayıs 1937); İran baytarî mukavelesi (Haziran 1937); Atatürk'ün çiftliklerini Hazine'ye bağışlaması (Haziran 1937).

| Tarih | Gazete, sayfa | Başlık / konu | Strand | Not |
|---|---|---|---|---|
| 1936-11-25 | *Cumhuriyet* 8 | **"Ağrı vilâyetinde baytarî çalışma: Hayvan hastalıklarının önüne tamamen geçildi"** | **S3** | "Vebayi bakarinin en ziyade memleketimize girdiği yer İran sınırlarıdır." İlkbaharda yaylaya çıkan hayvanlar "birer birer termometre muayenesinden" geçiriliyor, sonbaharda dönüşte muayene tekrarlanıyor. İran sınırından 15 km içerideki köylerin hayvanları yılda birkaç defa genel termometre muayenesinden geçiyor. Vesikasız ve baytar raporu olmadan sınırdan giren hayvanlar 21 gün **karantina** altına alınıyor. Kazalarda "küçük hayvan sağlık memurları" ayda 20 gün köy dolaşıyor. Sınır, yaylak ve göç S3'te aynı denetim pratiğinde birleşiyor |
| 1937-01-27 | *Cumhuriyet* 6 | İstanbul'da et | S0 | "İstanbul artık et yemesini unutmuş bir beldedir": et fiyatı ve kalite üzerine şehir yazısı |
| 1937-05-17 | *Cumhuriyet* 3 | Kars yolculuğu (röportaj) | S1, S4 | Rusların şose boyunca sıraladığı "dizme köyler"; dik çatılı evler. Kars düzünde yetişen hayvan miktarı "garbî Anadolu'nun hayvan yetiştiren on vilâyetinin iki misli". "İriyarı yakışıklı boğalar… benek benek kınalı" inekler: "Bunların buzağıları bile [Orta Anadolu'nun] öküzleri kadar." Doğu sınır bölgesi ıslah edilmiş sığırın yeri olarak sunuluyor (Kafkas ve Rus etkisi) |
| 1937-06-13 | *Cumhuriyet* 1, 7 | **Atatürk'ün çiftliklerini Hazine'ye bağışladığı mektup** | **S1** | Çiftlikler 13 yılda "yerli ve yabancı birçok hayvan ırkları üzerinde çift ve mahsul bakımından yaptıkları tetkikler neticesinde bunların muhite en elverişli ve verimli olanlarını tespit etmişler". Çevre köylerle kooperatif çalışma. Islahın **"model çiftlik" ayağı**: ırk denemesi devletin değil Reisicumhur'un şahsi çiftliklerinde yapılmış ve 1937'de devlete devredilmiş |
| 1937-06-20 | *Cumhuriyet* 2 (Şehir işleri) | **"Hayvanları bıçakla kesmek medenî bir usul değilmiş!"** | S3, S0 | İstanbul Baytar Müdüriyeti, mezbahada hayvanların "hisleri iptal edildikten sonra" öldürülmesi için belediyeye rapor verdi. Bayıltarak kesim tartışması "medenîlik" diliyle açılıyor |
| 1937-06-28 | *Cumhuriyet* 2 (Köyler ve köylüler) | **Bahri Turgud Okaygün, "Şarkî Anadolu'da köy evleri"** | **S4, S2** | Ev sahibiyle diyalog: yazar "daha geniş pencereli ve camlı" ev ve ayrı odalar öneriyor, köylü maliyeti ve kışı gerekçe gösteriyor. Ev damı "hem mutfak hem salon, hem yatak odası ve hem de kiler". **"Muş, Erzurum, Van ve Bitlis'in bir kısım köylerinde kış odaları vardır. Bunlar öküz, inek, katır, at ahırının bir tarafında yapılmış geniş ocaklı ve tahtaperde veya yarım kerpiç duvar… ile ayrılmış yerlerdir. Hem sıcak olurlar."** Ormansız ovada "ot, tezek ve saman yakarlar". Tezek: "hayvan gübreleri samanla karıştırılarak kalıp halinde yapılır ve güneşte kurutularak yığılır ve kışın yakılır." Hayvanlar meradan toplanan ot ve samanla besleniyor, ağır kışta "açlıklarından telef olup gider". Öneri: mera ve kışlağa önem verilmesi. "Şarkî Anadolu köylerinin en kıymetli varlıkları: Sığırlar" (ara başlık). **S4 için şimdiye kadarki en ayrıntılı basın tanıklığı: ahırla aynı mekânı paylaşan "kış odası", gübre yakacağı ve bunun yem ve kışla ilişkisi** |
| 1937-06-30 | *Cumhuriyet* 2 (aynı dizi, 7) | Şark vilâyetlerinde kışlak göçü | **S2** | Büyük sürüler "Mardin, Urfa ve Seruç havalisinin cenubundaki kışlaklara" (Berrî) gönderiliyor. Ağır kışta "çoban… köye eli boş, yüzü kara bir halde döner". Sürülerin kışlakta tek yiyeceği ovaların kurumuş otları. Köylüye sonbaharda meteoroloji bülteni gönderilmesi önerisi |

### Üçüncü parti (Mart–Nisan 1938)

Pencere: Hayvanlar Vergisi değişikliği (kaçakçılık, damızlık boğa; Mart 1938).

| Tarih | Gazete, sayfa | Başlık / konu | Strand | Not |
|---|---|---|---|---|
| 1938-03-17 | *Cumhuriyet* 2 (Şehir işleri) | "Mezbahada kesilen hayvanlar" (bir aylık) | S0 | 20.348 karaman, 16.949 kuzu… **1.365 öküz, 95 inek**, 240 malak, 217 manda, 25 boğa, 449 dana. Öküzün inekten 14 kat fazla kesilmesi, 1934 Mayıs verisindeki örüntüyü (1.860'a 209) tekrarlıyor |
| 1938-03-18 | *Cumhuriyet* 1 (Ankara, telefonla) | **"Büyük ziraat kongresi 18 Nisanda toplanıyor"** | **S0** | **FVADC'nin öncülü ya da ertelenmiş ilk biçimi.** Katılımcılar: Meclis ziraat ve iktisat encümeni üyeleri, Ziraat Vekâleti ve enstitülerinin mütehassıs, profesör ve doçentleri, haralar, fidanlıklar, "bakteriyolojihane" müdürleri, her vilâyet ziraat odasının seçeceği birer çiftçi ve "hayvan yetiştiricilerden mümessiller". Orman kongre dışında. Ruznamede "baytariye ve ziraate aid meseleler", pamuk, **silo** ve buğday var. Aynı haberde memleketin ziraat mıntakalarına ayrıldığı ve buralarda zirai istasyonlar kurulacağı bildiriliyor (sayı OCR'da okunmuyor). Kongrenin Nisan'dan Aralık 1938'e neden kaydığı (Atatürk'ün hastalığı? Celâl Bayar hükümetinin programı?) araştırılmalı: Mart–Nisan 1938 *Ayın Tarihi* ve TBMM tutanakları |
| 1938-04-10 | *Cumhuriyet* 4 | Küçük hikâye "Sarı Hüseyin" | S0, S3 | Köy meydanında çocuklar, eşeğe binip önüne birkaç sığır katmış bir adamın arkasından "kaçakçı, kaçakçı!" diye bağırıyor. Hayvan kaçakçılığı (vergi ve sınır) edebî metinde de figür olmuş. Aynı pencerede Hayvanlar Vergisi değişikliği kaçakçılığı hedefliyor |

## Ara değerlendirme

- **Muğla dizisi (1933, 1936, 1939) ıslahın yerelde nasıl kurulduğunu izlemeye imkân veriyor.**
  - 1933'te vilâyet meclisi üç damızlık aygırı bile gereksiz buluyor.
  - 1936'da vilâyet "öküz soyunun düzeltilmesi" için 9 boz ırk boğası alıyor.
  - 1939'da 50 örnek köy, 34 boğa ve 142 boğa siparişi var; yerli boğalar iğdiş ediliyor.
  - Bu, S1 için tek vilâyette yürüyen bir zaman çizgisi. Muğla, Trakya'dan sonra ikinci vaka çalışması adayı.
- **İstanbul et arzında öküz baskın.** Bu oran, sığırın önce çift hayvanı, sonra et olduğunu gösteriyor. İş gücü ile et arasındaki dönüşüm S0'ın merkezi.
- **S4, Doğu Anadolu'nun "kış odası":** Okaygün'ün 1937 yazısı, 1924 Köy Kanunu'nun ev ile ahırı ayırma hedefinin on üç yıl sonra doğuda nasıl karşılandığını gösteriyor. Ahırın bir köşesi, hayvan sıcaklığı için bilerek "kış odası" yapılıyor. Köylü cam ve oda bölmesine maliyet ve kış gerekçesiyle direniyor. Yakacak tezekten, yani yemle beslenen hayvanın gübresinden geliyor. Ev, hayvan, yem ve yakıt tek bir döngü. Bu, rapor 05'teki S4 hipotezini (ahır–ev birlikteliği bir "geri kalmışlık" değil, ısı ve yakıt ekonomisi) doğrudan destekliyor.
- **S3, sınır ve yayla:** Ağrı'da (1936) karantina yalnız sınır kapısında değil, **yaylaya çıkış ve dönüşte**, termometreyle tek tek uygulanıyor. Hayvanın hareketliliği (yaylak–kışlak) salgın denetiminin birimi oluyor.
- **Sıradaki:**
  - kalan *Cumhuriyet* pencereleri (1936–1943);
  - aynı pencereler için *Akşam*, *Tan* ve *Son Posta* listeleri;
  - "Mandıra ve Ağıllar Kanunu" (1929) penceresinin ayrıca okunması. Bu kanun, 1938 kongresinde istenen "ağıl kanununun tadili" (rapor 04, *Kurun* 1938-12-29) ile doğrudan bağlantılı.
