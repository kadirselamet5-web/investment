"""İBB Atatürk Kitaplığı dijital gazete sayılarını listeler, indirir ve OCR'lar.

Adımlar:
  liste  : bir başlığın belirli yıllardaki bütün e-sayılarını (demirbaş, eser adı, PDF adresi, tarih) çıkarır
  ocr    : listedeki sayılardan tarih aralığına düşenleri indirir, tesseract (tur) ile OCR'lar
           ve <cikti>/<gazete>/<YYYY-MM-DD>_<sayi>.txt olarak yazar (sayfalar \\f ile ayrılır); PDF silinir

Kullanım:
  python3 ibb_gazete.py liste "<Eser adı>" <yil1,yil2,...> <liste.tsv> [<bas YYYY-MM-DD> <bit YYYY-MM-DD>]
  python3 ibb_gazete.py ocr <liste.tsv> <baslangic YYYY-MM-DD> <bitis YYYY-MM-DD> <cikti_dizini> [--is 4]
                            [--pencereler <dosya>]  (çoklu tarih penceresi; bas/bit yok sayılır)

Tarih, PDF dosya adındaki 1938M0209 biçiminden okunur. İstekler arasında kısa bekleme yapılır.
"""
import base64
import html
import http.cookiejar
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pymupdf

KOK = "https://katalog.ibb.gov.tr/yordam/"
_cj = http.cookiejar.CookieJar()
_op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(_cj))
_nonce = None


def _al(url, deneme=4):
    for i in range(deneme):
        try:
            with _op.open(url, timeout=120) as r:
                return r.read()
        except Exception:
            if i == deneme - 1:
                raise
            time.sleep(2 ** (i + 1))


def _arama(eser, yil, sno):
    global _nonce
    fq = ['kunyeAnaTurKN_str:"0505"', f'kunyeSayiYil_str:"{yil}"']
    url = (KOK + "?p=1&dil=0&alan=qEser_txt&adet=50&q=" + urllib.parse.quote_plus(f'"{eser}"')
           + "".join("&fq[]=" + urllib.parse.quote_plus(f) for f in fq) + (f"&sno={sno}" if sno > 1 else ""))
    t = _al(url).decode("utf-8", "ignore")
    m = re.search(r"nonce=([0-9a-f]{16,})", t)
    if m:
        _nonce = m.group(1)
    kayitlar = re.findall(r'data-demirbas="([^"]*)" data-eseradi="([^"]*)"', t)
    sayfalar = [int(x) for x in re.findall(r"sno=(\d+)'", t)]
    return [(d, html.unescape(e)) for d, e in kayitlar], max(sayfalar or [1])


def _pdf(demirbas):
    url = (KOK + "sayfa/detay.php?dil=0&demirbas=" + demirbas + "&kiosk=&q=&tip=&mode=detayligorunum&nonce="
           + (_nonce or ""))
    t = _al(url).decode("utf-8", "ignore")
    m = re.search(r'data-json="([^"]*)"', t)
    if not m:
        return ""
    try:
        return json.loads(base64.b64decode(m.group(1)))[0]["dosya"]
    except Exception:
        return ""


def _detay(d):
    u = _pdf(d)
    m = re.search(r"_(\d{4})M(\d{2})(\d{2})_", u)
    time.sleep(0.3)
    return (f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ""), u


def liste(eser, yillar, cikti, bas=None, bit=None):
    """Arama sayfalarından sayıları toplar. bas/bit verilirse yalnızca o tarih aralığına düşmesi
    tahmin edilen sayıların ayrıntısı (tarih, PDF) alınır: her yılın en küçük ve en büyük sayısının
    tarihi alınıp sayı numarasından doğrusal tahmin yapılır (±10 sayı pay)."""
    tamam = set()
    if os.path.exists(cikti):
        tamam = {s.split("\t")[0] for s in open(cikti, encoding="utf-8")}
    f = open(cikti, "a", encoding="utf-8")
    for yil in yillar:
        sno, son, kayit = 1, 1, []
        while sno <= son:
            kayitlar, son = _arama(eser, yil, sno)
            for d, e in kayitlar:
                # yalnızca başlığı tam eşleşenler (ör. "Cumhuriyet. [1938 4937]", "Cumhuriyet Çocuğu" değil)
                if not re.match(re.escape(eser) + r"\.?\s*\[", e):
                    continue
                sayi = re.search(r"\[\s*\d{4}\s+(\d+)\s*\]", e)
                kayit.append((d, int(sayi.group(1)) if sayi else None))
            sno += 1
        print(eser, yil, len(kayit), "sayı listelendi", flush=True)
        secili = kayit
        if bas and bit and kayit:
            numarali = sorted((n, d) for d, n in kayit if n is not None)
            if len(numarali) >= 2:
                from datetime import date
                # uç değerlere (ör. "0" numaralı ek/ilave kayıtları) karşı %5'lik kırpma
                k = len(numarali) // 20
                (n1, d1), (n2, d2) = numarali[k], numarali[-1 - k]
                t1, t2 = _detay(d1)[0], _detay(d2)[0]
                if t1 and t2 and n2 > n1:
                    g1, g2 = date.fromisoformat(t1).toordinal(), date.fromisoformat(t2).toordinal()
                    hb, hs = date.fromisoformat(bas).toordinal(), date.fromisoformat(bit).toordinal()
                    oran = (g2 - g1) / (n2 - n1)
                    secili = [(d, n) for d, n in kayit if n is None or
                              hb - 10 * oran <= g1 + (n - n1) * oran <= hs + 10 * oran]
        for d, n in secili:
            if d in tamam:
                continue
            tarih, u = _detay(d)
            f.write(f"{d}\t{eser}\t{n or ''}\t{tarih}\t{u}\n")
            f.flush()
            tamam.add(d)
        print(eser, yil, len(secili), "sayının ayrıntısı alındı", flush=True)


def _ocr_sayfa(png):
    r = subprocess.run(["tesseract", png, "-", "-l", "tur", "--psm", "3"], capture_output=True, text=True,
                       env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    return r.stdout


def _hazirla(is_):
    """PDF'i indirir ve sayfaları PNG'ye çizer (OCR işçileriyle eşzamanlı çalışır)."""
    hedef, eser, tarih, sayi, url = is_
    tmp = tempfile.mkdtemp(prefix="ibb_")
    pdf = os.path.join(tmp, "s.pdf")
    open(pdf, "wb").write(_al(url))
    doc = pymupdf.open(pdf)
    pngler = []
    for i, p in enumerate(doc):
        png = os.path.join(tmp, f"{i:03d}.png")
        p.get_pixmap(dpi=250, colorspace=pymupdf.csGRAY).save(png)
        pngler.append(png)
    doc.close()
    os.remove(pdf)
    return is_, tmp, pngler


def ocr(liste_yolu, bas, bit, dizin, isci=4, pencereler=None):
    """bas/bit tek bir aralık verir; pencereler [(bas, bit), ...] verilirse bunlardan herhangi
    birine düşen sayılar işlenir.

    Boru hattı: sonraki sayılar arka planda indirilip çizilirken OCR işçileri iki sayının
    sayfalarını birlikte işler; böylece indirme ve sayfa sonu beklemelerinde CPU boşta kalmaz."""
    import shutil
    from collections import deque
    araliklar = pencereler or [(bas, bit)]
    isler = []
    for satir in open(liste_yolu, encoding="utf-8"):
        d, eser, sayi, tarih, url = satir.rstrip("\n").split("\t")[:5]
        if not tarih or not url or not any(b <= tarih <= s for b, s in araliklar):
            continue
        hedef_dizin = os.path.join(dizin, re.sub(r"\W+", "_", eser).strip("_"))
        os.makedirs(hedef_dizin, exist_ok=True)
        hedef = os.path.join(hedef_dizin, f"{tarih}_{sayi or d}.txt")
        if not os.path.exists(hedef):
            isler.append((hedef, eser, tarih, sayi, url))
    kalan = iter(isler)
    with ThreadPoolExecutor(isci) as havuz, ThreadPoolExecutor(2) as hazirlik:
        hazir, aktif = deque(), deque()

        def ileri():
            is_ = next(kalan, None)
            if is_:
                hazir.append(hazirlik.submit(_hazirla, is_))

        ileri(), ileri()
        while hazir or aktif:
            if hazir and len(aktif) < 2:
                f = hazir.popleft()
                ileri()
                try:
                    is_, tmp, pngler = f.result()
                except Exception as e:  # indirme/çizim hatası: sayı atlanır, sonraki koşuda yeniden denenir
                    print("HATA", e, flush=True)
                    continue
                aktif.append((is_, tmp, [havuz.submit(_ocr_sayfa, p) for p in pngler]))
                continue
            (hedef, eser, tarih, sayi, _), tmp, futs = aktif.popleft()
            metin = [f.result() for f in futs]
            open(hedef, "w", encoding="utf-8").write("\f".join(metin))
            shutil.rmtree(tmp, ignore_errors=True)
            print(eser, tarih, sayi, len(metin), "sayfa", flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "liste":
        pencere = sys.argv[5:7] if len(sys.argv) >= 7 else (None, None)
        liste(sys.argv[2], [int(y) for y in sys.argv[3].split(",")], sys.argv[4], *pencere)
    elif sys.argv[1] == "ocr":
        isci = int(sys.argv[sys.argv.index("--is") + 1]) if "--is" in sys.argv else 4
        pencereler = None
        if "--pencereler" in sys.argv:  # ibb_olay.py'nin yazdığı <liste>.pencereler dosyası
            yol = sys.argv[sys.argv.index("--pencereler") + 1]
            pencereler = [tuple(s.split("\t")[:2]) for s in open(yol, encoding="utf-8") if s.strip()]
        ocr(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], isci, pencereler)
