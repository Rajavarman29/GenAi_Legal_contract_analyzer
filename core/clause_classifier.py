def classify_clause(text):
    t = text.lower()
    if "shall" in t or "must" in t:
        return "Obligation"
    if "may" in t:
        return "Right"
    if "shall not" in t or "must not" in t:
        return "Prohibition"
    return "Other"
