import spacy

nlp = spacy.load("en_core_web_sm")

LIABILITY_TERMS = [
    "liable", "liability", "damages", "losses", "indemnify"
]

def extract_jurisdiction(text):
    triggers = ["governed by", "jurisdiction", "courts of"]
    for t in triggers:
        if t in text.lower():
            return text
    return None

def extract_liabilities(text):
    return [t for t in LIABILITY_TERMS if t in text.lower()]

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "PARTIES": [],
        "DATES": [],
        "AMOUNTS": [],
        "LOCATIONS": [],
        "JURISDICTION": None,
        "LIABILITIES": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["PARTIES"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["DATES"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["AMOUNTS"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["LOCATIONS"].append(ent.text)

    entities["JURISDICTION"] = extract_jurisdiction(text)
    entities["LIABILITIES"] = extract_liabilities(text)

    return entities
