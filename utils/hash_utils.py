import hashlib

def hash_document(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
