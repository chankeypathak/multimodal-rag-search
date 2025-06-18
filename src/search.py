import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.embed import embed_text

def search_knowledge_base(query, kb_path="knowledge_base.pkl", top_k=5):
    df = pd.read_pickle(kb_path)
    qvec = embed_text(query)
    scores = cosine_similarity([qvec], list(df["embedding"]))[0]
    df["score"] = scores
    return df.sort_values("score", ascending=False).head(top_k)

if __name__ == "__main__":
    results = search_knowledge_base("show me technical diagrams", top_k=3)
    print(results[["type", "source", "page", "content", "score"]])
