
class JDAgent:
    
    def __init__(self,retriever):
        self.retriever = retriever

    def run(self,resume):
        jobs = self.retriever.retrieve(resume)

        return jobs