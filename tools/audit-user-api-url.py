from pathlib import Path
root=Path("app-source/GudiyaTaxiPartner")
for p in root.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in (".html",".kt",".java",".xml",".json",".properties",".js"):
        continue
    try:
        lines=p.read_text(encoding="utf-8").splitlines()
    except Exception:
        continue
    hits=[(i,line) for i,line in enumerate(lines,1) if any(term in line.lower() for term in ("onrender.com","apiurl","api_base","api_base","gudiya_api_base","api_base_url","apiurl","evaluatejavascript","loadurl","config.js"))]
    if hits:
        print("\\nFILE:",p)
        for i,line in hits[:80]:
            print(str(i)+": "+line[:1200])
