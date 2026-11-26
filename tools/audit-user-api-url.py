from pathlib import Path
root=Path('app-source/GudiyaTaxiPartner')
for p in root.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in ('.html','.kt','.java','.xml','.json','.properties'):
        continue
    try:
        lines=p.read_text(encoding='utf-8').splitlines()
    except Exception:
        continue
    hits=[(i,line) for i,line in enumerate(lines,1) if 'onrender.com' in line.lower() or 'apiurl' in line.lower() or 'api_base' in line.lower() or 'const api' in line.lower()]
    if hits:
        print('\nFILE:',p)
        for i,line in hits[:50]:
            print(str(i)+': '+line[:1000])
