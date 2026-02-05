from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_clause(clause, templates):
    corpus = templates + [clause]
    tfidf = TfidfVectorizer().fit_transform(corpus)
    sims = cosine_similarity(tfidf[-1], tfidf[:-1])
    return sims.max()
