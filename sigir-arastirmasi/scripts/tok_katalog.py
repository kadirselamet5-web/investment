"""Tarım ve Orman Bakanlığı Kütüphanesi (VuFind) kataloğundan 1923–1950 yayınlarını toplar.

Uzmanlık ağı için: her sorgunun bütün sonuç sayfaları taranır, kayıt ayrıntısından yazar(lar),
yayın yeri, yayınevi, seri ve notlar alınır.
Kullanım: python3 tok_katalog.py <cikti.jsonl> <sorgu1> [<sorgu2> ...]
Çıktı JSONL; zaten alınmış kayıtlar atlanır (kaldığı yerden devam eder).
"""
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

KOK = "https://kutuphane.tarimorman.gov.tr/vufind/"
YIL = 'publishDate:"[1923 TO 1950]"'


def al(url, deneme=4):
    for i in range(deneme):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (academic research)"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception:
            if i == deneme - 1:
                raise
            time.sleep(2 ** (i + 1))


def temiz(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def sonuc_sayfasi(sorgu, sayfa):
    q = {"lookfor": sorgu, "type": "AllFields", "filter[]": YIL, "limit": "20", "page": str(sayfa)}
    t = al(KOK + "Search/Results?" + urllib.parse.urlencode(q))
    toplam = re.search(r"results of\s*<strong>?\s*([\d,.]+)", t) or re.search(r"results of\s+([\d,.]+)", re.sub(r"<[^>]+>", " ", t))
    idler = list(dict.fromkeys(re.findall(r'href="/vufind/Record/([^"/?#]+)" class="title', t)))
    return idler, int(re.sub(r"\D", "", toplam.group(1))) if toplam else 0


def kayit(rid):
    t = al(KOK + "Record/" + urllib.parse.quote(rid))
    alan = {}
    for m in re.finditer(r"<tr>\s*<th[^>]*>(.*?)</th>\s*<td[^>]*>(.*?)</td>\s*</tr>", t, re.S):
        alan[temiz(m.group(1)).rstrip(":")] = temiz(m.group(2))
    baslik = re.search(r'<h[1-3][^>]*property="name"[^>]*>(.*?)</h[1-3]>', t, re.S)
    cevrimici = re.findall(r'<th>Online Access:</th>\s*<td>(.*?)</td>', t, re.S)
    alan_link = re.findall(r'href="(https?://[^"]+)"', cevrimici[0]) if cevrimici else []
    yazarlar = [html.unescape(a) for a in re.findall(r'/vufind/Author/Home\?author=([^"&]+)', t)]
    yazarlar = list(dict.fromkeys(urllib.parse.unquote_plus(a).strip() for a in yazarlar))
    return {"id": rid, "baslik": temiz(baslik.group(1)) if baslik else "", "yazarlar": yazarlar, "alanlar": alan,
            "cevrimici": alan_link,
            "url": KOK + "Record/" + rid}


def main():
    cikti = sys.argv[1]
    alinan = set()
    if os.path.exists(cikti):
        alinan = {json.loads(s)["id"] for s in open(cikti, encoding="utf-8")}
    f = open(cikti, "a", encoding="utf-8")
    for sorgu in sys.argv[2:]:
        sayfa, toplam, bulunan = 1, None, 0
        while True:
            idler, n = sonuc_sayfasi(sorgu, sayfa)
            toplam = toplam or n
            for rid in idler:
                bulunan += 1
                if rid in alinan:
                    continue
                try:
                    k = kayit(rid)
                except Exception as e:  # noqa: BLE001
                    print("HATA", rid, e, flush=True)
                    continue
                k["sorgu"] = sorgu
                f.write(json.dumps(k, ensure_ascii=False) + "\n")
                f.flush()
                alinan.add(rid)
                time.sleep(0.3)
            if not idler or bulunan >= (toplam or 0):
                break
            sayfa += 1
        print(sorgu, "toplam", toplam, "görülen", bulunan, flush=True)


if __name__ == "__main__":
    main()
