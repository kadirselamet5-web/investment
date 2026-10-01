"""Site için metin paketleri ve PDF bağlantıları.

site_uret.py tarafından çağrılır. Önemli sayfaların/birimlerin tam metnini site/metin/<grup>.js
dosyalarına yazar (tarayıcıda istek üzerine yüklenir) ve her kayıt için
  m   : metin anahtarı (ya da anahtar listesi)
  pdf : doğrudan PDF bağlantısı (mümkünse #page=N ile)
döndürür. PDF bağlantıları için TBMM Açık Erişim (DSpace) ve Internet Archive API sonuçları
bulgular/pdf_baglantilari.json dosyasında önbelleklenir.

Seçim ölçütleri:
  tutanak : puanı >= 6 olan görüşme kümelerinin bütün sayfaları
  dergi   : puanı >= 6 olan birimler (3000 karakterlik parça, tara.py --parca 3000 ile aynı bölme)
  ocr     : OCR'lanan dergilerin bütün isabetli sayfaları
  gazete  : puanı >= 3 olan bütün gazete sayfaları
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict

TUTANAK_ESIK = 6.0
DERGI_ESIK = 6.0
PARCA = 3000


def _al_json(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (academic research)"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            if i == 3:
                return None
            time.sleep(2 ** (i + 1))


class Paket:
    def __init__(self, kok, calisma):
        self.kok, self.calisma = kok, calisma
        self.gruplar = defaultdict(dict)   # grup -> {anahtar: metin}
        self.dizin = {}                     # anahtar -> grup
        self.onbellek_yol = os.path.join(kok, "bulgular", "pdf_baglantilari.json")
        self.onbellek = json.load(open(self.onbellek_yol, encoding="utf-8")) if os.path.exists(self.onbellek_yol) else {}
        self._items = None
        self._metin_cache = {}

    # ------------------------------------------------------------ yardımcılar
    def ekle(self, grup, anahtar, metin):
        metin = re.sub(r"[ \t]+", " ", metin or "").strip()
        if not metin:
            return None
        self.gruplar[grup][anahtar] = metin
        self.dizin[anahtar] = grup
        return anahtar

    def dosya(self, yol):
        if yol not in self._metin_cache:
            if len(self._metin_cache) > 24:  # küçük önbellek: büyük IA metinleri tekrar tekrar okunmasın
                self._metin_cache.pop(next(iter(self._metin_cache)))
            self._metin_cache[yol] = open(yol, encoding="utf-8", errors="replace").read() if os.path.exists(yol) else None
        return self._metin_cache[yol]

    def items(self):
        if self._items is None:
            p = os.path.join(self.calisma, "tbmm_dspace", "items.json")
            self._items = {x["handle"]: x for x in json.load(open(p))} if os.path.exists(p) else {}
        return self._items

    def dspace_pdf(self, handle, ad):
        """TBMM Açık Erişim: handle + dosya adı -> bitstream içerik bağlantısı."""
        k = "dspace:" + handle
        if k not in self.onbellek:
            it = self.items().get(handle)
            harita = {}
            if it:
                b = _al_json(f"https://acikerisim.tbmm.gov.tr/server/api/core/items/{it['uuid']}/bundles")
                for bu in (b or {}).get("_embedded", {}).get("bundles", []):
                    if bu["name"] != "ORIGINAL":
                        continue
                    bs = _al_json(bu["_links"]["bitstreams"]["href"] + "?size=1000") or {}
                    for x in bs.get("_embedded", {}).get("bitstreams", []):
                        harita[x["name"]] = x["_links"]["content"]["href"]
            self.onbellek[k] = harita
        harita = self.onbellek[k]
        return harita.get(ad) or harita.get(ad.replace(".txt", "")) or (next(iter(harita.values())) if len(harita) == 1 else "")

    def ia_dosyalar(self, kimlik):
        k = "ia:" + kimlik
        if k not in self.onbellek:
            d = _al_json(f"https://archive.org/metadata/{urllib.parse.quote(kimlik)}/files") or {}
            adlar = [f["name"] for f in d.get("result", [])]
            txt = [n for n in adlar if n.endswith("_djvu.txt")]
            self.onbellek[k] = [(n[:-9] + ".pdf") if (n[:-9] + ".pdf") in adlar else "" for n in txt]
        return self.onbellek[k]

    def kaydet(self):
        json.dump(self.onbellek, open(self.onbellek_yol, "w", encoding="utf-8"), ensure_ascii=False)
        d = os.path.join(self.kok, "site", "metin")
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):
            if f.endswith(".js") and f[:-3] not in self.gruplar:
                os.remove(os.path.join(d, f))
        for g, v in self.gruplar.items():
            js = "window.__metin(" + json.dumps(g) + "," + json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ");"
            yol = os.path.join(d, g + ".js")
            if not os.path.exists(yol) or open(yol, encoding="utf-8").read() != js:
                open(yol, "w", encoding="utf-8").write(js)

    # ------------------------------------------------------------ kaynaklar
    def tutanak(self, kume):
        """kume: tbmm_tutanak_gorusme_kumeleri.csv satırı (sözlük). Anahtar listesi ve PDF bağlantısı döndürür."""
        ad = os.path.basename(kume["pdf_url"])[:-4]
        sayfalar = [int(x) for x in re.findall(r"\d+", kume["pdf_sayfalar"])]
        ilk, son = (sayfalar[0], sayfalar[-1]) if sayfalar else (1, 1)
        pdf = f"{kume['pdf_url']}#page={ilk}"
        if float(kume["toplam_puan"] or 0) < TUTANAK_ESIK:
            return [], pdf
        ham = self.dosya(os.path.join(self.calisma, "tbmm", "text", ad + ".txt"))
        if not ham:
            return [], pdf
        s = ham.split("\f")
        grup = "t_" + (re.search(r"tbmm(\d\d)", ad).group(1) if re.search(r"tbmm(\d\d)", ad) else "x")
        anahtarlar = [self.ekle(grup, f"t:{ad}:{p}", s[p - 1]) for p in range(ilk, min(son, len(s)) + 1)]
        return [a for a in anahtarlar if a], pdf

    def dergi(self, r):
        """dergi_isabetleri.csv satırı -> (anahtar, pdf, konum_notu)."""
        no = int(r["sayfa_veya_parca"])
        if r["platform"] == "Internet Archive":
            yol = os.path.join(self.calisma, "ia", "text", r["dosya"] + ".txt")
        else:
            h = r["kayit_url"].split("/handle/")[-1]
            yol = os.path.join(self.calisma, "tbmm_dspace", "text", h.replace("/", "_"), r["dosya"] + ".txt")
        ham = self.dosya(yol)
        if not ham:
            return "", r["kayit_url"], ""
        birim, toplam, konum, sayfa = [], 0, 0, 1
        for pi, s in enumerate(ham.split("\f"), 1):
            for i in range(0, max(len(s), 1), PARCA):
                birim.append((pi, i, len(s)))
        if no > len(birim):
            return "", r["kayit_url"], ""
        pi, ofs, uz = birim[no - 1]
        sayfa_metni = ham.split("\f")[pi - 1]
        metin = sayfa_metni[ofs:ofs + PARCA]
        yuzde = f"belgede yaklaşık %{round(100 * ofs / max(uz, 1))} konumunda"
        if r["platform"] == "Internet Archive":
            dosyalar = self.ia_dosyalar(r["dosya"]) if float(r["puan"]) >= DERGI_ESIK else []
            pdf_ad = dosyalar[pi - 1] if pi - 1 < len(dosyalar) else ""
            terim = (r["terimler"].split(";")[0].split("/")[0].split(" (")[0]) if r["terimler"] else ""
            pdf = (f"https://archive.org/download/{r['dosya']}/{urllib.parse.quote(pdf_ad)}" if pdf_ad
                   else f"https://archive.org/details/{r['dosya']}?q={urllib.parse.quote(terim)}")
            konum = f"dosya {pi}, {yuzde}"
        else:
            pdf = (self.dspace_pdf(r["kayit_url"].split("/handle/")[-1], r["dosya"]) if float(r["puan"]) >= DERGI_ESIK
                   else "") or r["kayit_url"]
            konum = yuzde
        anahtar = ""
        if float(r["puan"]) >= DERGI_ESIK:
            grup = ("d_ia_" if r["platform"] == "Internet Archive" else "d_tb_") + (r["yil"][:3] or "x")
            anahtar = self.ekle(grup, f"d:{r['platform'][:2]}:{r['dosya']}:{no}", metin) or ""
        return anahtar, pdf, konum

    def ocr_dergi(self, r):
        h = r["kayit_url"].split("/handle/")[-1]
        yol = os.path.join(self.calisma, "tbmm_ocr", h.replace("/", "_"), r["dosya"] + ".txt")
        ham = self.dosya(yol)
        p = int(r["pdf_sayfa"])
        pdf = self.dspace_pdf(h, r["dosya"])
        pdf = f"{pdf}#page={p}" if pdf else r["kayit_url"]
        if not ham:
            return "", pdf
        s = ham.split("\f")
        return (self.ekle("o_" + h.replace("/", "_"), f"o:{h}:{r['dosya']}:{p}", s[p - 1]) if p <= len(s) else ""), pdf

    def gazete(self, gazete, tarih, sayi, sayfa, pdf_url):
        dizin = re.sub(r"\W+", "_", gazete).strip("_")
        for kok in (os.path.join(self.calisma, "ibb", "metin"), os.path.join(self.calisma, "ibb", "olay", "metin"),
                    os.path.join(self.calisma, "ibb", "dergi", "metin")):
            ham = self.dosya(os.path.join(kok, dizin, f"{tarih}_{sayi}.txt"))
            if ham:
                break
        pdf = f"{pdf_url}#page={sayfa}" if pdf_url else ""
        if not ham:
            return "", pdf
        s = ham.split("\f")
        p = int(sayfa)
        return (self.ekle(f"g_{dizin}_{tarih[:7]}", f"g:{gazete}:{tarih}_{sayi}:{p}", s[p - 1]) if p <= len(s) else ""), pdf
