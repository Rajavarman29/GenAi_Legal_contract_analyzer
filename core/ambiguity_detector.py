AMBIGUOUS_TERMS = [
    "reasonable",
    "as applicable",
    "sole discretion",
    "from time to time",
    "as deemed fit"
]

def detect_ambiguity(text):
    found = []
    for term in AMBIGUOUS_TERMS:
        if term in text.lower():
            found.append(term)
    return found
