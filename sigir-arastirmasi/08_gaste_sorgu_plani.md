# Gaste Arşivi Sorgu Planı (Tur 2, Chrome oturumu için)

Bu dosya, kullanıcının Claude in Chrome ile oturum açılmış **Gaste Arşivi**'ne bağladığı oturumda çalıştırılacak sorguların planıdır. Sorguların tam listesi ve takip sütunları `08_gaste_sorgu_listesi.csv` dosyasında; liste `scripts/gaste_sorgu_uret.py` ile üretildi (terim ya da olay eklemek için betik düzenlenip yeniden çalıştırılır).

## 0. Tur 2 güncellemesi: İBB ile örtüşme

İBB Atatürk Kitaplığı'nın açık dijital koleksiyonu (bkz. `06_kaynak_envanteri.md`, Tur 2 eki) *Cumhuriyet*, *Tan/Milliyet*, *Akşam*, *Vakit/Kurun*, *Son Posta*, *Haber* ve *Yeni Sabah*'ın 1923–1942 sayılarını içeriyor. Bu yüzden:

- **Blok A (FVADC penceresi)** İBB PDF'leri üzerinden OCR ile yapılıyor (`scripts/ibb_gazete.py`; 15 Kasım 1938 – 28 Şubat 1939; 7 gazete). Gaste Arşivi'nde bu blok yalnızca *Ulus* için ve karşılaştırma için çalıştırılacak.
- **Blok B ve C** için İBB'de bulunan gazete ve yıllar yerel OCR ile taranabilir. Gaste Arşivi öncelikle **İBB'de olmayanlara** ayrılır: *Ulus* (1934–50), 1943–1950 bütün gazeteler, *Yeni Asır*, *Son Telgraf*, taşra gazeteleri.

## 1. Oturum protokolü

1. **Envanter (ilk 15 dakika):** Gaste Arşivi'ndeki gazeteler ve yıl aralıkları listelenir, `06_kaynak_envanteri.md`'ye işlenir. Özellikle şunlar kontrol edilir:
   - *Hâkimiyet-i Milliye/Ulus*, *Cumhuriyet*, *Akşam*, *Vakit/Kurun*, *Milliyet/Tan*, *Son Posta*, *Yeni Sabah*, *Vatan*, *Tasvir*, *Yeni Asır*;
   - Arap harfli sayılarda (1923–1928) OCR araması olup olmadığı.
2. **Arama dizimi testi:** tırnaklı ifade, joker (`sığır*`), Türkçe karakter duyarlılığı ("sigir" ile "sığır" aynı sonucu veriyor mu?), tarih ve gazete süzgeçleri. Sonuç `02_anahtar_kelime_tezaurusu.md` §A'ya not düşülür.
3. **Pilot (Faz 0'ın ertelenen adımı):** 1938 yılı, 20 çekirdek terim. Her terim için ilk 20 isabet açılır; isabet/gürültü oranı hesaplanır; gürültülü terimler (ör. "yem" → "yemin", "şap" → "şapka", "hara" → "harap") için dışlama kuralı yazılır.
4. **Sorgu çalıştırma sırası:** Blok A → B → C → D (aşağıda). Her sorguda CSV'deki `isabet_sayisi`, `acilan`, `ilgili` ve `durum` sütunları doldurulur. Her oturum `05_arama_gunlugu.csv`'ye tek satır olarak da işlenir.
5. **Kayıt:** İlgili her haber, `03_kayit_sablonu.csv` biçiminde `bulgular/gazete_kayitlari.csv`'ye yazılır: gazete, tarih, sayfa, sütun, başlık, strand, terimler, özet, önemli alıntı ve görüntü bağlantısı. **Seçki yapılmaz:** ilgili olan her haber kayda girer; yalnızca açıkça ilgisiz olanlar (ilan, şiir, soyadı eşleşmesi vb.) elenir ve eleme nedeni günlüğe sayı olarak yazılır.
6. **Çok isabet veren sorgular:** Bir yıl–terim sorgusu 300'den fazla isabet verirse gazete gazete, gerekirse çeyrek yıllara bölünür. Bölünen satırlar CSV'ye yeni `sorgu_no` ile eklenir (ör. G0412a).

## 2. Bloklar

| Blok | Satır | Öncelik | İçerik |
|---|---|---|---|
| **A: FVADC penceresi** | 29 | 1 | Kongre 27 Aralık 1938'de Başvekil Celal Bayar'ın nutkuyla açıldı. (1) Haziran 1938 – Mart 1939 arasında 8 kongre sorgusu, bütün gazetelerde. (2) 15 Kasım 1938 – 28 Şubat 1939 arasında 7 gazetenin **sayfa sayfa göz taraması**, 3 ay dilimi × 7 gazete. Komisyon raporları, delege konuşmaları, köylü mektupları, karikatürler ve sonraki yorumlar aranır |
| **B: Olay pencereleri** | 46 | 1 (1929+), 2 (1923–28) | Tur 1'de TBMM'de bulunan 46 kilit görüşme ve kanun: görüşmeden 2 hafta önce – 4 hafta sonra, olaya özgü terimlerle. 1928 öncesi pencereler Arap harfli basında **göz taraması** |
| **C: Çekirdek terimler × yıl** | 814 | 2 | 37 ★ terim (OCR varyantlarıyla) × 1929–1950 arası her yıl, bütün gazeteler. Asıl "tek tek bütün haberler" taraması budur |
| **D: Kişi ve kurum adları** | 18 | 3 | Spöttel, Gebhardt, Falke, YZE, Pendik, Etlik, haralar, Ziraat Vekilleri, OIE vb.; 1923–1950 |

## 3. Tahmini iş yükü

- **Blok A:** 1938–39 günlük gazetelerde gün başına 6–12 sayfa var. 7 gazete × 105 gün, yaklaşık 5.000–8.000 sayfa eder. Göz taraması en ağır kalem; sayfa başına 5–10 saniyeyle yaklaşık 10–20 saat.
- **Blok C:** Tur 1 TBMM oranlarına göre "sığır", "ahır" ve "yem" gibi terimler yılda yüzlerce isabet verebilir. Isabet sayıları önce toplu çıkarılır (yalnızca sonuç sayısı), sonra en yoğun yıllardan başlanarak isabetler açılır.
- Tur 2'de hedef: **Blok A ve B'nin tamamı, Blok C'de D3 dilimi (1934–1939)**. Kalanı Tur 3'e kalır.

## 4. Chrome oturumunda dikkat edilecekler

- Kullanıcının abonelik bilgileri ve oturum çerezleri hiçbir dosyaya yazılmaz.
- Görüntü indirme hakkı ve kullanım şartları ilk oturumda kontrol edilir. Yalnızca bağlantı, künye ve kısa alıntı saklanır.
- Hızlı ve çok sayıda istek hesabı kilitleyebilir; sorgular arasında insan hızında bekleme yapılır.
- Cumhuriyet Arşivi (Cumhuriyet gazetesinin kendi arşivi) ayrı bir abonelikse, *Cumhuriyet* için aynı liste orada çalıştırılır.
