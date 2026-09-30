# İlerleme Takibi

`[ ]` başlanmadı · `[~]` sürüyor / kısmen · `[x]` bitti · `[!]` erişim engeli · `–` kapsam dışı

## Tur 1 özeti (2026-09-30)

| Faz | Durum | Ne yapıldı | Sonuç | Dosya |
|---|---|---|---|---|
| 0 Altyapı | [x] | Tezaurus v1.0 makinece aranır hale getirildi (`scripts/terimler.py`, 89 terim grubu). Gürültü testleri yapıldı (tezek/tezekkür, yem/yemin, veba/vebal ayrıldı). Tarama ve puanlama betikleri yazıldı | — | `scripts/` |
| 1 TBMM tutanakları | [x] tur 1 | 2.–9. dönem (Ağu 1923 – Tem 1950) 2.575 birleşimin tamamı indirildi ve tarandı. 643 yüksek puanlı küme okundu; 77 kilit görüşme seçildi | 13.274 sayfa, 7.052 küme | `bulgular/01_…`, `bulgular/tbmm_tutanak_*.csv` |
| 1 Resmî Gazete / Düstur | [~] | Düstur 3. tertip (TBMM Açık Erişim, OCR'lı ciltler) tarandı | `dergi_isabetleri.csv` içinde | `bulgular/02_…` §4 |
| 2A–2B Ulusal günlük gazeteler | [!] | Gaste Arşivi ve Cumhuriyet Arşivi abonelik ve Cloudflare nedeniyle erişilemedi. **Vekil kaynaklar tarandı:** *Ayın Tarihi* (1937, 1939–46), *Beyoğlu* (Fransızca, 1939–44), *Atayolu* (1948–49), TBMM'deki tek sayılar | — | `bulgular/02_…` §2, §6 |
| 2C FVADC penceresi | [~] | FVADC Komisyonlar Mazbatası tarandı. Kongre yayınlarının tam metinleri Tarım ve Orman Bakanlığı kütüphanesinde, **üye girişi gerekiyor**. Gazete penceresi (1938 – Mart 1939) günlük gazeteler olmadan yapılamadı | — | `bulgular/02_…` §5 |
| 3 Mesleki dergiler | [~] | *Askerî Tıbbî Baytarî Mecmuası* 1929–1937 tam tarandı (Latin harfli kısım). *Türk Baytarlar Cemiyeti Mecmuası*, YZE yayınları ve Ziraat Vekâleti Neşriyatı çevrimiçi bulunamadı | 712 güçlü parça | `bulgular/02_…` §1 |
| 4 Halkevi dergileri ve monografiler | [~] | *Ülkü* (3 seri, tamamı), 30'dan fazla halkevi dergisi (TBMM ve IA), *Halk Bilgisi Haberleri*, *Kadro*, Berkes 1942 (OCR'landı). **Tesseract OCR sürüyor:** 49 kaydın 3'ü bitti | binlerce parça | `bulgular/02_…` §3, §5 |
| 5 Yerel gazeteler | [~] | TBMM Açık Erişim'deki yerel gazeteler envantere alındı. 1924–28 sayıları Arap harfli (göz taraması). 1938–50 sayıları OCR kuyruğunda. Milli Kütüphane yurt dışından erişilemiyor | — | `bulgular/02_…` §7 |
| 6 İngilizce basın | [~] | Papers Past tamamlandı (2.088 aday, 14 ilgili). Chronicling America, HathiTrust, Trove, *The Times* ve JSTOR'a erişilemedi | 14 makale | `bulgular/03_…` |
| 7 Uluslararası kurumlar | [ ] | Tutanaklarda Milletler Cemiyeti veteriner sözleşmelerine atıflar bulundu (Bulgaristan 1934, Yunanistan 1939). LONTAD taranmadı | — | — |
| 8 Eğitim materyali ve edebiyat | [~] | *Muğla Halkevi Dergisi*'ndeki baytar öğütleri dizisi ve *6 Ok*'taki Köy Kanunu açıklamaları bulundu | — | `bulgular/02_…` |

## Tur 2 için öncelik sırası

1. **Günlük gazeteler (en büyük boşluk).** İki yol var:
   - (a) Gaste Arşivi aboneliğiyle aramaları kullanıcı yapar ve sonuç listelerini dışa aktarır; ben kaydeder ve kodlarım.
   - (b) Kullanıcının kendi tarayıcısına bağlı bir araçla (Claude in Chrome) oturum açılmış Gaste Arşivi'nde sorguları ben çalıştırırım.

   Sorgu listesi hazır: `02_anahtar_kelime_tezaurusu.md` içindeki ★ terimler × gazeteler × dönem dilimleri.
2. **OCR kuyruğunu bitirmek** (`scripts/tbmm_ocr.py`): kalan 46 kayıt. *Kaynak* (Balıkesir), *Çorumlu*, *Erciyes*, *Görüşler*, *Derme* (Malatya), *Erzurum*, *Hatay Devleti Resmî Gazetesi* ve 1938–50 yerel gazeteleri. Ardından `scripts/tara.py` ile tarama.
3. **Tutanaklarda ikinci OCR turu:** 1936–38 metinlerinde Türkçe karakterler bozuk ("Tiirkiye", "sigir", "§"). Terim listesine bu varyantlar eklenerek aynı yıllar yeniden taranacak.
4. **Arap harfli göz taraması:**
   - *Ziraat Vekâleti Mecmuası* (1924–25), en öncelikli kaynak;
   - *Ayın Tarihi* (1923–29);
   - *Askerî Tıbbî Baytarî Mecmuası* (1923–28);
   - 1924–1928 yerel gazeteleri (*Diyarbekir*, *Urfa*, *Mamüretülaziz*, *Malatya*);
   - TBMM eski harfli asıl tutanaklarından yalnızca, Latin çevriyazısı eksik olan birleşimler.
5. ***Askerî Tıbbî Baytarî Mecmuası* ve *Ülkü* için tam içindekiler dökümü:** makale başlığı, yazar ve yıl. Fihrist sayfaları (ATBM p1678, p2278, p2464, p2013) bulundu.
6. **FVADC yayınları:** Tarım ve Orman Bakanlığı Kütüphanesi'ne üye girişiyle 51 PDF indirilip taranacak.
7. **Faz 7:** LONTAD'da 1935 Cenevre veteriner sözleşmeleri ve Türkiye dosyaları.
8. **İngilizce:** Kurumsal erişimle *The Times* (Ankara muhabiri), *Near East and India*, *Commerce Reports*, *Foreign Crops and Markets*.

## Erişim durumu (Tur 1'de doğrulandı)

| Kaynak | Durum |
|---|---|
| TBMM tutanakları (www5.tbmm.gov.tr) | ✓ açık; PDF'lerin metin katmanı iyi |
| TBMM Kütüphanesi Açık Erişim (DSpace 7 API) | ✓ açık; 3.679 kayıt, 1923–50 arası 658 kayıt; 490'ının OCR'ı yok |
| Internet Archive | ✓ açık |
| DigitalNZ / Papers Past API | ✓ açık |
| Tarım ve Orman Bakanlığı Kütüphanesi | ~ katalog açık; PDF'ler üye girişi istiyor |
| APİKAM (İzmir) | ~ açık; gazete fonu katalog düzeyinde, OCR araması bulunamadı |
| Gaste Arşivi, Chronicling America, HathiTrust | ✗ Cloudflare (ve Gaste Arşivi için abonelik) |
| Papers Past web arayüzü | ✗ Incapsula (API üzerinden erişildi) |
| Milli Kütüphane, Hakkı Tarık Us, tarihigazete.com | ✗ yanıt yok (yurt dışı erişim engeli olabilir) |
| SALT Araştırma, İÜ Nadir Eserler | ✗ 403 |
