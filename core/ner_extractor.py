import spacy

def load_spacy_model():
    """
    Loads the spaCy English model.
    If the model is not available (e.g., on Streamlit Cloud),
    it downloads it at runtime and then loads it.
    """
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

LIABILITY_TERMS = [
    "liable",
    "liability",
    "damages",
    "losses",
    "indemnify",
    "indemnification"
]

def extract_jurisdiction(text):
    """
    Detect jurisdiction-related clauses using rule-based triggers.
    """
    triggers = [
        "governed by",
        "jurisdiction",
        "courts of",
        "subject to the laws of"
    ]
    text_lower = text.lower()
    for t in triggers:
        if t in text_lower:
            return text
    return None

def extract_liabilities(text):
    """
    Extract liability-related terms from the clause text.
    """
    text_lower = text.lower()
    return [term for term in LIABILITY_TERMS if term in text_lower]

def extract_entities(text):
    """
    Extract named entities and legal-relevant information from contract text.
    """
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
