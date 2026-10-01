# Gaste Arşivi oturumu: talimat (yerel Claude + Claude in Chrome için)

Bu dosya, kullanıcının **kendi bilgisayarında** çalışan ve **Claude in Chrome** ile Gaste Arşivi'ne (oturum açılmış) erişen Claude oturumu içindir. Bulut oturumu Chrome'a erişemez. Bulut oturumu bu oturumun ürettiği dosyaları her saat çeker, raporlara, zaman çizelgesine ve siteye işler.

## 0. Hazırlık

```bash
git clone https://github.com/kadirselamet5-web/investment.git
cd investment
git checkout claude/charming-hawking-ggi8hy
cd sigir-arastirmasi
```

Okunacaklar (kısa): `01_arastirma_programi.md` (dört strand: S1 ıslah ve üreme, S2 yem ve mera, S3 hastalık, karantina ve sınır, S4 ev, ahır ve tezek; S0 çapraz), `08_gaste_sorgu_plani.md` (protokol), `08_gaste_sorgu_listesi.csv` (907 sorgu).

## 1. Kurallar

- **Abonelik bilgisi, çerez ya da parola hiçbir dosyaya yazılmaz.** Ekran görüntüsü yalnızca haber kırpıntısı olarak alınır.
- **İnsan hızında çalış:** sorgular arasında birkaç saniye bekle, toplu indirme yapma, sitenin kullanım koşullarına uy. Site engel ya da uyarı gösterirse dur ve kullanıcıya bildir.
- Haber metnini olduğu gibi aktar. OCR ve okuma hatalarını düzeltirken `[?]` ile işaretle, uydurma.

## 2. Sıra (öncelik)

1. **Envanter (ilk iş, yaklaşık 15 dk):** Gaste'de hangi gazete ve yıllar var? `bulgular/gaste/envanter.md`'ye yaz. Özellikle *Ulus/Hâkimiyet-i Milliye*, *Vatan*, *Tasvir*, *Yeni Asır* ve 1943–1950 yılları. Arama dizimini de test et: tırnaklı ifade, joker, "sigir" ile "sığır" farkı.
2. **Blok A, yalnız *Ulus*:** 15 Kasım 1938 – 28 Şubat 1939 (kongre dönemi; öteki 7 gazete bulut oturumunda OCR ile bitti). Sorgular: `blok == A-FVADC` satırları, gazete süzgeci Ulus.
3. **Blok B (olay pencereleri):** önce İBB'de olmayanlar: *Ulus* (1934–1943) ve **1931 olayları** (Islah-ı Hayvanat Kanunu 4. madde tadili, Mart 1931; Davar ve Ehlî Hayvanlar Vergisi, Haziran–Temmuz 1931).
4. **Öncelikli doğrulamalar:**
   - Ocak 1942: **"hayvanların dişlerini söküyorlar"** (kesim yasağını delmek için). *Tan*, *Akşam*, *Vatan*, *Ulus*.
   - Mart–Nisan 1938: **18 Nisan 1938'e planlanan "Büyük Ziraat Kongresi"** neden Aralık'a ertelendi?
   - **"Ağıl kanunu"** (1929 Mandıra ve Ağıllar Kanunu; 1938'de tadil talebi).
5. **1944–1950 bütün gazeteler:** Blok C'de `baslangic >= 1944` satırları (İBB'de yok).
6. Kalan Blok C ve Blok D satırları, `oncelik` sırasıyla.

## 3. Çıktılar (bulut oturumu bunları okur)

Her şeyi `sigir-arastirmasi/bulgular/gaste/` altına yaz:

- **`gaste_kayitlari.csv`**: ilgili her haber bir satır. Başlık satırı `03_kayit_sablonu.csv` ile aynı: `kayit_id,strand,ilgi_derecesi,kaynak_turu,yayin_adi,tarih,sayi,sayfa,sutun,baslik,yazar,tur,eslesen_terimler,yer_adlari,kisi_kurum,ozet,kisa_alinti,erisim_yeri,goruntu_dosyasi,durum,not`.
  - `kayit_id` biçimi `GA0001`, `GA0002`, …
  - `tarih` YYYY-AA-GG; `ilgi_derecesi` 1 (çok önemli), 2 veya 3.
  - `ozet` 1–3 cümle; `kisa_alinti` en çarpıcı 1–2 cümle (birebir).
  - `erisim_yeri` haberin Gaste bağlantısı (kalıcı bağlantı varsa).
- **`metin/<gazete>_<tarih>_s<sayfa>.txt`**: önemli (ilgi 1–2) haberlerin tam metni, sitenin okuyucusunda gösterilecek.
- **`08_gaste_sorgu_listesi.csv`**: çalıştırılan her sorgunun `isabet_sayisi`, `acilan`, `ilgili` ve `durum` (`[x]`) sütunlarını doldur.
- **`05_arama_gunlugu.csv`**: her oturum sonunda bir satır (`arama_id` `G` ile başlasın: `G0001`…; veritabani = "Gaste Arşivi").

## 4. Kaydet ve gönder

Her 30–60 dakikada bir ve oturum sonunda:

```bash
git add sigir-arastirmasi/bulgular/gaste sigir-arastirmasi/08_gaste_sorgu_listesi.csv sigir-arastirmasi/05_arama_gunlugu.csv
git commit -m "Gaste: <ne yapıldı>"
git pull --rebase origin claude/charming-hawking-ggi8hy
git push origin claude/charming-hawking-ggi8hy
```

Yalnızca yukarıdaki dosyalara yaz. Öteki dosyaları (raporlar, site, scripts) bulut oturumu günceller; çakışma olmasın.

## 4a. Yerel oturum yoksa: yalnız Claude in Chrome yan paneli

Git kullanılamaz. Sonuçlar iki yoldan biriyle buluta ulaşır:

- **(a) Kullanıcı aracılığıyla:** her 10–20 kayıtta bir, kayıtları `gaste_kayitlari.csv` başlığıyla **CSV metni** olarak ver. Kullanıcı bunu bulut oturumuna yapıştırır ya da `.csv` dosyası olarak yükler.
- **(b) GitHub web arayüzü** (kullanıcı Chrome'da GitHub'a girişliyse): `github.com/kadirselamet5-web/investment/tree/claude/charming-hawking-ggi8hy/sigir-arastirmasi/bulgular/gaste` altında `gaste_kayitlari.csv` dosyasını oluştur ya da düzenle (satır ekle) ve aynı dala commit et. Başka dosyaya dokunma.

## 5. Kısa başlangıç komutu (kullanıcı yerel oturuma yapıştırır)

> `sigir-arastirmasi/GASTE_TALIMAT.md` dosyasını oku ve uygula. Chrome'da Gaste Arşivi oturumum açık. Envanterle başla, sonra Ulus'un kongre dönemine geç. Her saat başı commit ve push yap.
