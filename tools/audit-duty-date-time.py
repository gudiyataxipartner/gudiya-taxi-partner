from pathlib import Path
import re
p=Path("app-source/GudiyaTaxiPartner/app/src/main/assets/index.html")
s=p.read_text(encoding="utf-8")
for term in ["async function editDuty", "async function postDuty", "function apiDutyCard(d)", "function dutyMessage(d)", "function resetDutyForm", "dutyDate:date", "dutyTime:time"]:
    print("\\n===== "+term+" =====")
    for m in list(re.finditer(re.escape(term),s))[:2]:
        print(s[max(0,m.start()-250):min(len(s),m.start()+4200)])
