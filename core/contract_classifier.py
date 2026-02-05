def classify_contract(text):
    keywords = {
        "Employment": ["employee", "salary", "termination"],
        "NDA": ["confidential", "non-disclosure"],
        "Lease": ["rent", "premises", "lease"],
        "Partnership": ["partner", "profit sharing"],
        "Vendor": ["services", "deliverables", "payment"]
    }

    scores = {k: 0 for k in keywords}
    for k, words in keywords.items():
        for w in words:
            if w.lower() in text.lower():
                scores[k] += 1

    return max(scores, key=scores.get)
