# -*- coding: utf-8 -*-
from pathlib import Path
import re

repo = Path(__file__).parent
required = ["cyberleakgta6.com", "CyberLeak", "Q2 2022", "113", "FAQ"]
langs = ["", ".ru", ".es", ".de", ".fr", ".it", ".pt", ".pl", ".zh", ".ja", ".ko", ".tr"]

print("README verification:\n")
all_ok = True
for suf in langs:
    f = repo / f"README{suf}.md"
    text = f.read_text(encoding="utf-8")
    missing = [k for k in required if k not in text]
    faq = len(re.findall(r"\*\*(?:A|O|R|О|Ответ):\*\*", text))
    if faq < 14:
        faq = len(re.findall(r"^### (?:Q:|F:|В:|P:|D:|S:|O:|C:|K:|问:|質問:|Soru:)", text, re.M))
    ok = not missing and faq >= 14 and len(text.splitlines()) >= 400
    if not ok:
        all_ok = False
    print(f"{f.name}: {len(text.splitlines())} lines | FAQ items: {faq} | missing: {missing or 'none'} | {'OK' if ok else 'ISSUE'}")

print("\n" + ("ALL 12 README FILES OK" if all_ok else "SOME FILES NEED REVIEW"))
