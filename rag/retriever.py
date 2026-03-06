from rag.embedding import Embedding
from rag.vector_store import VectorStore




class JDRetriever():

    def __init__(self, jobs):
        self.embedder = Embedding()
        job_emb = self.embedder.embed(jobs)

        dim = len(job_emb[0])

        self.vector_store = VectorStore(dim)

        

    def retrieve(self, resume):
        resume_emb = self.embedder.embed([resume])[0]
        result  = self.vector_store.search(resume_emb, k=2)
        
        return result
    

