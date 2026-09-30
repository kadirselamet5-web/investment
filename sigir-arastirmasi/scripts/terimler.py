"""Tezaurus v1.0'ın makinece aranabilir hali (bkz. 02_anahtar_kelime_tezaurusu.md).

Her terim: (etiket, strand, düzenli ifade). Metin önce `normalize` ile küçük harfe çevrilir
(Türkçe İ/I kuralıyla), satır sonu tirelemeleri birleştirilir, düzeltme işaretleri kaldırılır.
OCR'ın Türkçe harfleri düşürdüğü durumlar için ı/i, ş/s, ğ/g, ç/c, ö/o, ü/u ikililerini
kabul eden karakter sınıfları kullanılır; gürültülü terimlerde (ahır/ahir, şap/sap, yem/yemin)
yalnızca doğru imla ya da dar ek listesi kabul edilir.
"""
import re

I = "[ıi]"
S_ = "[şs]"
G = "[ğg]"
C = "[çc]"
O = "[öo]"
U = "[üu]"
E = r"(?:[a-zçğıöşü]{0,8})"  # serbest ek
B = r"(?<![a-zçğıöşüâîû])"  # kelime başı

TERIMLER = [
    # S0 genel
    ("sığır", "S0", B + f"s{I}{G}{I}r" + E),
    ("inek", "S0", B + r"inek(?:ler|leri|lerin|lerden|in|i|e|te|ten|çi|çilik)?\b"),
    ("öküz", "S0", B + f"{O}k{U}z" + E),
    ("manda (hayvan)", "S0", B + r"manda(?:lar|ları|ların|lara|lardan)\b"),
    ("buzağı", "S0", B + f"buza{G}[ıiu]" + E),
    ("dana/düve/tosun", "S0", B + r"(?:dana|düve|tosun)(?:lar|ları|ların)?\b"),
    ("büyükbaş", "S0", B + f"b{U}y{U}k ?ba{S_}" + E),
    ("hayvancılık", "S0", B + f"hayvanc{I}l{I}k" + E),
    ("hayvan serveti", "S0", B + r"hayvan servet" + E),
    ("hayvanat", "S0", B + r"hayvanat" + E),
    ("hayvan yetiştir", "S0", B + f"hayvan(?:lar)? yeti{S_}tir" + E),
    ("hayvan sayımı", "S0", B + f"hayvan(?:lar)? say{I}m" + E),
    ("hayvanlar vergisi", "S0", B + r"hayvanlar vergi" + E),
    ("canlı hayvan", "S0", B + f"canl{I} hayvan" + E),
    ("hayvan ihracatı", "S0", B + r"hayvan(?:at)? ihracat" + E),
    ("celep", "S0", B + r"celep(?:ler|lerin|lik)?\b"),
    ("mezbaha/salhane", "S0", B + r"(?:mezbaha|salhane)" + E),
    ("et fiyatı/meselesi", "S0", B + f"et (?:fiyat|narh|meselesi|buhran|pahal{I}|istihsal|ihtiyac|ithal|ihrac)" + E),
    ("süt", "S0", B + f"s{U}t(?:[ çc]{U}l{U}k|l[eü]k|ler|ün|ü|tozu| fabrika| istihsal| verim)?\\b"),
    ("mandıra", "S0", B + f"mand{I}ra" + E),
    ("tereyağı/peynir", "S0", B + r"(?:tereyağ|peynir)" + E),
    ("deri/sakatat", "S0", B + r"(?:sakatat|işkembe|bağırsak ihrac)" + E),
    ("köy ve ziraat kalkınma", "S0", B + f"(?:k{O}y ve ziraat kalk{I}nma|ziraat kalk{I}nma kongre)" + E),
    ("ziraat kongresi", "S0", B + r"ziraat kongre" + E),
    # S1 üreme ve ırk ıslahı
    ("ırk/cins ıslahı", "S1", B + f"(?:{I}rk|cins|nesil|nesl|hayvan|s{I}{G}{I}r|at) {I}slah" + E),
    ("ıslahı nesil", "S1", B + f"{I}slah[ıi]? ?nes[il]" + E),
    ("damızlık", "S1", B + f"dam{I}zl{I}k" + E),
    ("boğa", "S1", B + r"boğa(?:lar|ları|ların|lara|nın|yı|ya|dan|sı|sını|ların)?\b"),
    ("aygır", "S1", B + f"ayg{I}r" + E),
    ("hara", "S1", B + r"hara(?:lar|ları|ların|sı|sına|sında|sından|nın|ya|da|dan)?\b"),
    ("Karacabey", "S1", B + r"karacabey" + E),
    ("Çifteler", "S1", B + f"{C}ifteler" + E),
    ("Sultansuyu", "S1", B + r"sultansuyu" + E),
    ("Orman Çiftliği", "S1", B + f"orman {C}iftli{G}" + E),
    ("Montafon/Şvits/Simental", "S1", B + r"(?:montafon|[şs]vi[çct]s|schwyz|simm?ental|holştayn|holstein|holşteyn|cersi|jersey|algav|allgäu)" + E),
    ("yerli ırk", "S1", B + f"yerli {I}rk" + E),
    ("kültür ırkı", "S1", B + f"k{U}lt{U}r {I}rk" + E),
    ("boz ırk/kara sığır", "S1", B + f"(?:boz {I}rk|kara s{I}{G}{I}r|k{I}rm{I}z{I} s{I}{G}{I}r|kilis s{I}{G}{I}r)" + E),
    ("melez/istavroz", "S1", B + r"(?:melez|istavroz)" + E),
    ("tereddi", "S1", B + r"tereddi(?:si|sine|ye|yi|den|nin)?\b"),
    ("suni telkih/tohumlama", "S1", B + r"(?:sun['’]?[iî] (?:telkih|tohumlama)|telkih istasyon)" + E),
    ("iğdiş/kastrasyon", "S1", B + f"(?:i{G}di{S_}|kastrasyon|burdizzo)" + E),
    ("zootekni", "S1", B + r"zoote[ck]ni" + E),
    ("hayvan sergisi", "S1", B + r"(?:hayvan|damızlık|sığır) sergi" + E),
    # S2 yem, açlık, mera
    ("yem", "S2", B + r"(?<!tayinat ve )yem(?:ler|leri|lerin|lik|i|e|den|de| bitki| nebat| kıtlı| darlı)?\b(?! bedel| istihkak| ve tayinat| kanun)"),
    ("yem (ordu tayinatı/bedeli)", "S2", B + r"(?:tayinat ve yem|yem (?:bedel|istihkak|ve tayinat|kanun))" + E),
    ("yonca", "S2", B + r"yonca" + E),
    ("silo/silaj", "S2", B + r"(?:silo|silaj|ensilaj|siloj)" + E),
    ("mera", "S2", B + r"mer['’]?a(?:lar|ları|ların|lara|larda|lardan|sı|ya|da|dan|nın)?\b"),
    ("otlak/yaylak/kışlak", "S2", B + r"(?:otlak|yaylak|kışlak)" + E),
    ("çayır", "S2", B + f"{C}ay{I}r" + E),
    ("kuru ot", "S2", B + r"kuru ot" + E),
    ("saman/kesmik", "S2", B + r"(?:saman|kesmik)(?:lar|ı|ın|dan)?\b"),
    ("küspe/posa/kepek", "S2", B + r"(?:küspe|pancar posa|melas|kepek)" + E),
    ("korunga/fiğ/burçak", "S2", B + r"(?:korunga|fiğ|burçak)" + E),
    ("hayvan kırılması", "S2", B + r"(?:hayvan(?:lar)?(?:ın)? kırıl|kış kırgın|kırgın|kıran)" + E),
    ("hayvan ölümü", "S2", B + r"hayvan(?:lar)?(?:ın)? öl" + E),
    ("kuraklık/kıtlık", "S2", B + r"(?:kuraklık|kıtlık)" + E),
    # S3 hastalık, veteriner, sınır
    ("baytar", "S3", B + r"baytar" + E),
    ("veteriner", "S3", B + r"veteriner" + E),
    ("sığır vebası", "S3", B + f"(?:s{I}{G}{I}r vebas|veba[iı]? ?bakar)" + E),
    ("veba (hayvan)", "S3", B + r"veba(?:sı|si|yı|yi|ya|dan|nın|i|ı)?(?: ?bakar[iı])?\b"),
    ("şap", "S3", B + r"şap(?: hastal|\b)" + E),
    ("şarbon/karakabarcık", "S3", B + r"(?:şarbon|karakabarcık|yanıkara)" + E),
    ("piroplazmoz/teileri", "S3", B + r"(?:piroplazm|theiler|teiler|babesi|kene humma)" + E),
    ("bruselloz/yavru atma", "S3", B + r"(?:brusell|bang hastal|yavru atma)" + E),
    ("tüberkülin/sığır veremi", "S3", B + r"(?:tüberkülin|sığır verem)" + E),
    ("sakağı", "S3", B + r"sakağı" + E),
    ("salgın/epizooti", "S3", B + r"(?:hayvan salgın|salgın hayvan|epizoot|sari hayvan)" + E),
    ("karantina", "S3", B + r"karantina" + E),
    ("hudut baytarı", "S3", B + r"hudut baytar" + E),
    ("sağlık zabıtası", "S3", B + r"sağlık zabıta" + E),
    ("serum/aşı (hayvan)", "S3", B + r"(?:serum darülistihzar|serum laboratuvar|serum enstit|serum ve aşı|aşı ve serum)" + E),
    ("Pendik/Etlik", "S3", B + r"(?:pendik|etlik)(?: bakteriyoloji| serum| veteriner| baytar| laboratuvar| enstit)" + E),
    ("bakteriyolojihane", "S3", B + r"bakteriyolojihane" + E),
    ("hayvan kaçakçılığı", "S3", B + r"(?:hayvan kaçak|kaçak hayvan)" + E),
    ("aşiret/göçebe", "S3", B + r"(?:aşiret|göçebe|konar ?göçer)" + E),
    # S4 ahır-ev
    ("ahır", "S4", B + r"ahır(?:lar|ları|ların|ı|ın|a|da|dan|la)?\b"),
    ("tezek", "S4", B + r"tezek(?:ler|leri|i|in|le|ten|lik)?\b"),
    ("gübre", "S4", B + r"gübre" + E),
    ("köy kanunu", "S4", B + r"köy kanun" + E),
    ("köy evi", "S4", B + r"(?:köy evleri|köy evi|köylü evleri|köylünün evi|köy binaları)" + E),
    ("hayvanla bir arada", "S4", B + r"hayvan(?:lar)?(?:ı|la|ıyla|larla|larıyla)? (?:beraber|bir arada|aynı)" + E),
    ("tandır", "S4", B + r"tandır" + E),
]

DERLENMIS = [(e, s, re.compile(r)) for e, s, r in TERIMLER]

# Sayfa puanı için ağırlıklar: 3 = doğrudan sığır/büyükbaş, 1 = hayvancılık genel, 0.3 = idari/bütçe veya çok anlamlı.
CEKIRDEK = {"sığır", "inek", "öküz", "manda (hayvan)", "buzağı", "dana/düve/tosun", "büyükbaş", "boğa", "sığır vebası", "şap",
            "Montafon/Şvits/Simental", "boz ırk/kara sığır", "yerli ırk", "kültür ırkı", "ırk/cins ıslahı", "suni telkih/tohumlama",
            "iğdiş/kastrasyon", "zootekni", "hayvan sergisi", "yonca", "silo/silaj", "tüberkülin/sığır veremi", "bruselloz/yavru atma",
            "piroplazmoz/teileri", "hudut baytarı", "hayvan kaçakçılığı", "hayvanla bir arada", "köy evi", "ahır", "tezek",
            "hayvan kırılması", "hayvan ölümü", "celep", "mandıra", "köy ve ziraat kalkınma", "Karacabey", "Çifteler",
            "Sultansuyu", "hayvan serveti", "hayvancılık", "hayvan yetiştir", "hayvan sayımı", "kuru ot", "korunga/fiğ/burçak"}
ZAYIF = {"yem (ordu tayinatı/bedeli)", "silo/silaj", "kuraklık/kıtlık", "aygır", "tereddi", "veba (hayvan)", "aşiret/göçebe",
         "saman/kesmik", "çayır", "gübre", "tandır", "süt", "tereyağı/peynir", "köy kanunu"}


def agirlik(etiket):
    return 3.0 if etiket in CEKIRDEK else 0.3 if etiket in ZAYIF else 1.0

_TR = str.maketrans({"İ": "i", "I": "ı", "â": "a", "î": "i", "û": "u", "Â": "a", "Î": "i", "Û": "u", "­": ""})


def normalize(metin):
    metin = re.sub(r"\u00ad\s*\n\s*", "", metin)  # yumuşak tire ile bölünmüş kelime
    metin = metin.translate(_TR).lower()
    metin = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", metin)  # satır sonu tireleme
    metin = re.sub(r"[ \t]*\n[ \t]*", " ", metin)
    return re.sub(r"[ \t]+", " ", metin)


# --- Türkçe harfleri düşmüş OCR metinleri için "katlanmış" (ASCII) kip ---
# 1935 sonu – 1937 tutanaklarında ü→"ii", ş→"§"/"sj", ı→i, ğ→g, ç→c, ö→o dönüşümleri görülüyor.
_KATLA = str.maketrans({"ı": "i", "ğ": "g", "ş": "s", "ç": "c", "ö": "o", "ü": "u", "â": "a", "î": "i", "û": "u", "§": "s"})


def katla(metin):
    metin = normalize(metin)
    metin = metin.replace("ii", "ü").replace("sj", "s")
    return metin.translate(_KATLA)


DERLENMIS_KATLI = [(e, s, re.compile(r.translate(_KATLA))) for e, s, r in TERIMLER]
