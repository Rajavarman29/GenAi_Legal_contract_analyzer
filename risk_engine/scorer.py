from risk_engine.rules import RISK_RULES

def score_clause(text):
    score = 0
    flags = []

    for risk, terms in RISK_RULES.items():
        for t in terms:
            if t in text.lower():
                flags.append(risk)
                score += 15

    if score >= 40:
        level = "High"
    elif score >= 20:
        level = "Medium"
    else:
        level = "Low"

    return level, min(score, 100), flags

def contract_score(scores):
    if not scores:
        return 0
    return int(min(sum(scores) / len(scores), 100))
