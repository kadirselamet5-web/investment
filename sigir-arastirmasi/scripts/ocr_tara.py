"""tbmm_ocr.py çıktısını tara.py ile tarar ve bulgular/dergi_isabetleri_ocr.csv'yi üretir.

Kullanım: python3 ocr_tara.py <items.json> <ocr_dizini> <calisma_dizini> <cikti.csv> [--esik 3]
Yalnızca tamamlanmış kayıtlar taranır (log'da sonraki kayda geçilmiş ya da iş bitmiş olanlar,
yani dizinindeki txt sayısı ORIGINAL paketindeki PDF sayısına eşit olanlar değil; basitçe mevcut txt'ler).
"""
import csv
import json
import os
import re
import subprocess
import sys

items, ocr, calisma, cikti = sys.argv[1:5]
esik = float(sys.argv[sys.argv.index("--esik") + 1]) if "--esik" in sys.argv else 3.0
kayit = {x["handle"]: x for x in json.load(open(items))}
duz = os.path.join(calisma, "duz")
os.makedirs(duz, exist_ok=True)
meta = open(os.path.join(calisma, "meta.tsv"), "w", encoding="utf-8")
for d in sorted(os.listdir(ocr)):
    yol = os.path.join(ocr, d)
    if not os.path.isdir(yol):
        continue
    handle = d.replace("_", "/", 1)
    ad = kayit.get(handle, {}).get("name", handle)
    for f in os.listdir(yol):
        if not f.endswith(".txt"):
            continue
        hedef = os.path.join(duz, f"{d}__{f}")
        if not os.path.exists(hedef):
            os.symlink(os.path.join(yol, f), hedef)
        yil = re.search(r"(18|19|20)\d\d", f)
        meta.write(f"{d}__{f[:-4]}\t{ad}\t{yil.group(0) if yil else ''}\n")
meta.close()
ham = os.path.join(calisma, "isabet.csv")
subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "tara.py"), duz, ham,
                "--meta", os.path.join(calisma, "meta.tsv")], check=True)
w = csv.writer(open(cikti, "w", newline="", encoding="utf-8"))
w.writerow(["yayin", "yil", "dosya", "pdf_sayfa", "puan", "strandlar", "terimler", "kayit_url", "baglam"])
n = 0
for r in csv.DictReader(open(ham, encoding="utf-8")):
    if float(r["puan"]) < esik:
        continue
    d, dosya = r["dosya"].split("__", 1)
    w.writerow([r["kaynak"], r["tarih"][:4], dosya.replace(".txt", ""), r["sayfa"], r["puan"], r["strandlar"],
                r["terimler"], "https://acikerisim.tbmm.gov.tr/handle/" + d.replace("_", "/", 1), r["baglam"]])
    n += 1
print(n, "satır (puan >=", esik, ")")
