import json
from collections import Counter

KB_PATH = "audit/sme_issues.json"

def update_kb(risk_flags):
    try:
        with open(KB_PATH, "r") as f:
            data = Counter(json.load(f))
    except:
        data = Counter()

    data.update(risk_flags)

    with open(KB_PATH, "w") as f:
        json.dump(data, f, indent=2)
