import faiss
import numpy as np


class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings))
        self.texts.extend(texts)

    def search(self, query_embedding, k):

        if len(self.texts) == 0:
            return []

        k = min(k, len(self.texts))

        D, I = self.index.search(
            np.array([query_embedding]), k
        )

        results = []

        for i in I[0]:
            if 0 <= i < len(self.texts):
                results.append(self.texts[i])

        return results