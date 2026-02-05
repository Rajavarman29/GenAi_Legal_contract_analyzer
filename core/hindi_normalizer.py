from llm.llm_client import call_llm

def normalize_hindi(text):
    prompt = f"""
    Translate the following Hindi legal contract into clear English.
    Preserve clause structure.
    Do NOT summarize.
    Text:
    {text}
    """
    return call_llm(prompt)
