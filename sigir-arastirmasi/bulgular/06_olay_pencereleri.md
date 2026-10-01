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

## Ara değerlendirme

- **Muğla dizisi (1933, 1936, 1939) ıslahın yerelde nasıl kurulduğunu izlemeye imkân veriyor.**
  - 1933'te vilâyet meclisi üç damızlık aygırı bile gereksiz buluyor.
  - 1936'da vilâyet "öküz soyunun düzeltilmesi" için 9 boz ırk boğası alıyor.
  - 1939'da 50 örnek köy, 34 boğa ve 142 boğa siparişi var; yerli boğalar iğdiş ediliyor.
  - Bu, S1 için tek vilâyette yürüyen bir zaman çizgisi. Muğla, Trakya'dan sonra ikinci vaka çalışması adayı.
- **İstanbul et arzında öküz baskın.** Bu oran, sığırın önce çift hayvanı, sonra et olduğunu gösteriyor. İş gücü ile et arasındaki dönüşüm S0'ın merkezi.
- **Sıradaki:**
  - kalan *Cumhuriyet* pencereleri (1936–1943);
  - aynı pencereler için *Akşam*, *Tan* ve *Son Posta* listeleri;
  - "Mandıra ve Ağıllar Kanunu" (1929) penceresinin ayrıca okunması. Bu kanun, 1938 kongresinde istenen "ağıl kanununun tadili" (rapor 04, *Kurun* 1938-12-29) ile doğrudan bağlantılı.
