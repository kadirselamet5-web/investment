# FVADC Gazete Penceresi (15 Kasım 1938 – 28 Şubat 1939): Bulgular — Tur 2, ara rapor

## Kaynak ve yöntem

- **Kaynak:** İBB Atatürk Kitaplığı dijital süreli yayın koleksiyonu (açık erişim, `katalog.ibb.gov.tr/yordam`). Yedi İstanbul gündelik gazetesi: *Cumhuriyet*, *Tan*, *Akşam*, *Kurun/Vakit*, *Son Posta*, *Yeni Sabah*, *Haber Akşam Postası*. Pencerede gazete başına yaklaşık 103 sayı, toplam yaklaşık 720 sayı.
- **Yöntem:** PDF'ler (metin katmanı yok) 250 dpi gri tonlamayla tesseract `tur` ile OCR'landı (`scripts/ibb_gazete.py`). Metinler tezaurus v1.0 ile tarandı (`scripts/tara.py`). Puanı ≥6 olan sayfalar tek tek okundu.
- **Katalog tarih hatası:** İBB kataloğunda gazetelerin Kasım 1938 sayıları dosya adlarında "Nisan 1938" olarak kayıtlı. Örneğin *Cumhuriyet* 5202–5226 numaralı sayıların gerçek tarihi 6–30 Kasım 1938. Tarihler sayı numarasından yeniden hesaplandı (`scripts/ibb_tarih_duzelt.py`) ve OCR metnindeki gazete başlığından doğrulanacak.
- **Durum:** *Cumhuriyet* 1 Aralık 1938 – 28 Şubat 1939 bitti (87 sayı; 252 sayfa puan ≥3, 55 sayfa puan ≥6). *Tan* sürüyor. 15–30 Kasım sayıları ile öteki beş gazete sırada.
- *Ulus* (Ankara) bu koleksiyonda yok; Gaste Arşivi oturumunda taranacak.

## *Cumhuriyet*: öne çıkan haberler

| Tarih | Sayfa | Başlık / konu | Strand | Not |
|---|---|---|---|---|
| 1938-12-09 | 6 | İsmet İnönü'nün Kastamonu gezisi (Daday): köylülerle konuşmalar | S0 | Çömlekçiler köyünden Karakaş Mehmed "öküzü yoktu, tarlası yoktu", amele olarak çalışıyor. "Arazim olsa rençperlik edeceğim." Vali ayrıca cüzzamlı köyü anlatıyor |
| 1938-12-11 | 7 | İnönü–köylü konuşmaları (Küre) | S0, S2 | Küney köyünden çiftçi Raşid: 30 davar, 8 sığır, 2 inek, 12 dönüm arazi. "Evimi asıl besliyen hayvanlardır. Bizim arazimiz kötüdür." Hayvanlar "arpa, siyez, yaprakla" besleniyor. Kuru ot tarladan geliyor; "ot" samandan iyi besliyor. Peynir yapmayı bilmiyorlar |
| 1938-12-13 | 7 | İnönü–köylü konuşmaları (Çerkeş) | S2, S0 | Bayındır köyünden bir köylü: "Yonca yetiştirir misiniz? — Otumuz bol… ihtiyacımız olmadığından yapmıyoruz." İnönü yoncanın tecrübe edilmesini "emretti". Köylü, çifte koşulan öküzlerin sayım vergisinden muaf tutulmasını istedi. İnönü: "Çift öküzlerile diğerlerini ayırmak kabil olsa, vergiyi çoktan kaldıracaktık" |
| 1938-12-14 | 5 | "Ege'de şap hastalığı vak'aları görüldü" | **S3** | İzmir ve Muğla'daki bütün hayvan iskeleleri çift tırnaklı hayvan ve hayvan maddeleri ihracatına kapatıldı. İzmir'in et ihtiyacı için hayvanlar karayoluyla değil, kapalı vagonlarla doğrudan mezbahaya gönderilecek |
| 1938-12-16 | 9 | Ziraat enstitüsü gençlerinin kabulü; "köy kalkınma planı ve ziraat kongresi" hakkında Reisicumhur'a izahat | S0 | Köy kalkınmasının resmî devlet planına başlıca mevzu olarak alınması |
| 1938-12-18 | 3 | (1) Ziraat Vekâleti'nin kongre tebliği ve valilere telgraf. (2) **Romanya göçmenleri Sincan'da** | S0, **S1, S4** | 98 hane (400 kişi) "bir damızlık boğa, 129 inek, manda, buzağı, 333 kıvırcık koyun" getirdi. "Üzerleri Marsilya benzeri kiremidlerle örtülü… bir zahire odası ve **ahırı** ihtiva eden kârgir evlere" yerleştirildiler. Hayvanlarına 10.000 kg saman ve 13.390 kg arpa verildi |
| 1938-12-30 | 9 | "Bu akşam Ziraat Kalkınma Kongresi kapanıyor" | S0 | Komisyonların gece geç saatlere kadar çalışması |
| 1938-12-31 | 1, 7 | Kongrenin son günü: komisyon mazbataları okundu | **S1, S2** | **Hayvan İşleri** mazbatası: "sayım vergisinin kaldırılması, boğa ihtiyacının temini için alınması lâzım gelen kararlar", atçılık dilekleri. **Hayvan Yemi** komisyonu mazbatası. Bir takrirde "manda cinsinin vikayesi". Oturum başkanı Eskişehir Eşrefiye köyünden bir köylü |
| 1939-01-06 | 5 | "Birinci Köy ve Ziraat Kalkınma Kongresi"nin encümen temennileri: şeker pancarı fiyatları | S0 | Yorum yazısı |
| 1939-01-06 | 6 | "Memlekette süt işi nasıl halledilecek? İneklerimizin bol süt vermediği anlaşıldığı için…" (Bursa) | **S1** | Süttozu fabrikası "memleketimizde bol süt veren hayvanların az yetişmekte" olduğunu tespit etmiş. Fabrika 1934'ten beri Romanya'dan **Montafon** cinsi inek getiriyor. Karacabey Harası'nın "mücavir köyler halkının hayvanları üzerinde oynadığı muslih rol" |
| 1939-01-11 | 5 | "Silolarımız": kongrenin başlıca mevzularından biri | S2 | Burada "silo" hububat silosu anlamında (Toprak Mahsulleri Ofisi) |
| 1939-01-14 | 5 | Mersin'de et fiyatları | S0 | Kasapların kesimi azaltması üzerine belediye narhı artırdı: sığır ve dana eti 15'ten 18 kuruşa (koyun 35, keçi 25) |
| 1939-01-20 | 5 | Et ve süt meselesi: Devlet Ziraat İşletmeleri Kurumu'nun İstanbul mezbahasında "nâzım rol"ü | S0 | Kurum günde 30–40 koyundan 400 koyun kesimine çıktı. Süt işinde de aynı yol izlenecek (Ziraat Vekili Faik Kurdoğlu) |
| 1939-02-08 | 2 | "Et meselesi": DZİK yeni tedbirler | S0 | Kurum İstanbul'un et ihtiyacının %25'inden fazlasını kesmeyecek. "Şimdiye kadar kesilmiyen dana ve sığır da kesilecektir" |
| 1939-02-16 | 7 | İstanbul Belediyesi'nin mezbahayı ıslahı | S0 | — |
| 1939-02-18 | 10 | Pendik Bakteriyoloji Enstitüsü'nden açık artırmayla hayvan satışı (öküz, kısrak, eşek) | S3 | İlan |
| 1939-02-20 | 12 | Bir müesseseye "çiçek aşısına elverişli 150 aded dana" alınacak | S3 | Aşı üretiminde dana kullanımı (ilan) |
| 1939-02-21 | 10 | Karacabey Harası hekimlik kadrosu ilanı | S1 | İlan |
| 1939-02-24 | 10 | Kayseri Belediyesi mezbaha inşaatı eksiltmesi (100.471 lira) | S0 | İlan |

## *Tan*: öne çıkan haberler (1–24 Aralık 1938; OCR sürüyor)

| Tarih | Sayfa | Başlık / konu | Strand | Not |
|---|---|---|---|---|
| 1938-12-11 | 9 | **"Her Köye Boğa Alınıyor"** (Kayseri) | **S1** | "Her köy namına birer damızlık boğa alınması kalkınma programına ithal edilmiş, şimdiye kadar (195) boğa alınmıştır." İlde 552 köy var; kalan köylerin boğaları iki yılda alınacak, "boğasız köy kalmıyacaktır". Boğalar Kayseri'deki damızlık ineklerin cinsine uygun olarak "bilhassa Erzurum havalisinden getirtilmektedir" |
| 1938-12-14 | 7, 9 | İnönü'nün Çerkeş'te köylülerle konuşmaları (Cumhuriyet 13 Aralık'ın *Tan* versiyonu, daha ayrıntılı) | S0 | Muhtar Mehmet Tarhan: 90 dönüm, 90 koyun, 100 keçi, "beş ineğim, dört öküzüm, mandam var", iki kısrak, iki merkep, "eski babadan kalma sapan". Bir başka köylünün 70–80 hayvanı ve bir çift öküzü var, ineği yok |
| 1938-12-18 | 9 | **"Şap Hastalığı Görüldü"** (Bozüyük) | **S3** | İlçe baytarı ile vilayetten gönderilen iki baytar köylere çıktı. Kaza kordon altına alındı, hayvan giriş-çıkışı durduruldu, "hayvan pazarı da muvakkaten kaldırılmıştır" |
| 1938-12-18 | 1, 8 | Kongre tebliği: 4 gün sürecek; yılbaşı gecesi resepsiyon | S0 | Anadolu Ajansı tebliği |
| 1938-12-19 | 2 | Sincan'daki Romanya göçmenleri (bkz. *Cumhuriyet* 18 Aralık) | S1, S4 | Aynı AA haberi |
| 1938-12-22 | 7 | **"Kongrenin Çalışma Mevzuları"**: 11 komisyon ve gündemleri | S0–S3 | Hayvan Yemi Komisyonu: "tabii ve suni çayırlar, yemlik bakliyat". Hayvanat Komisyonu: "mücadele, suni ve tabii tohumlama, hayvan mahsullerinin kıymetlendirilmesi… atçılık, sığırcılık, davarcılık, kümes hayvanları, tavşan" |
| 1938-12-22 | 7 | "Büyük Ziraat Kongresinden Köylü Neler Bekliyor?" dizisi: bir sütçünün sözleri | S0 | Köylü inek sütünü şehre götüremiyor; aracılar köyden 10 kuruşa alıp suyla çoğaltarak şehirde 25 kuruşa satıyor. Dizi kongre öncesi dilekleri topluyor; bütün bölümleri ayrıca taranacak |
| 1938-12-22 | 1, 8 | "Ziraat Kongresi Hazırlıkları": inşaatı süren bir devlet çiftliği | S1 | Çiftlik "bin hayvan ile çalışmıya" başlayacak, sayı beş bine çıkarılacak; damızlık tavşan şubesi. Milli Sanayi Birliği'nin kongre raporları (deri, yün, süt, süt tozu) |

Tam liste (puan ≥3, 252 sayfa, OCR bağlam parçalarıyla) bütün gazeteler bitince `fvadc_gazete_isabetleri.csv` olarak eklenecek. Gürültü örnekleri: tefrika romanlarda "yabani öküz", "su aygırı", "boğa(z)"; ilan ve tarihî yazılar.

## Ara değerlendirme

- Kongre haberleri (18, 30, 31 Aralık) gazetede Anadolu Ajansı tebliği biçiminde, kısa çıkıyor. Hayvan İşleri Komisyonu'nun iki talebi (sayım vergisinin kaldırılması ve boğa temini), TBMM'deki Komisyonlar Mazbatası ile aynı (rapor 02 §5).
- Aynı haftalarda İnönü'nün Kastamonu gezisindeki köylü konuşmaları, sığırın köy ekonomisindeki yerini köylünün ağzından veriyor ("evimi asıl besliyen hayvanlardır"). Yonca ve sayım vergisi konularının Reisicumhur düzeyinde tartışılması, S2 ve S1 için kongreyle eşzamanlı bir ikinci kaynak.
- Sincan göçmen köyü haberi, devletin göçmenlere "ahırlı kârgir ev" ile birlikte damızlık boğa ve inek yerleştirmesini gösteriyor. S4 (ev–ahır mimarisi) ve S1 için somut bir örnek.
