from utils.loader import load_jobs
from rag.retriever import JDRetriever
from agents.jd_agent import JDAgent
from agents.ats_agent import ATSAgent



def run_pipeline(resume):

    jobs = load_jobs("data/job_descriptoins_data.txt")

    retriever  =JDRetriever(jobs)

    jd_agent = JDAgent(retriever)

    ats_agent = ATSAgent()

    match_jobs = jd_agent.run(resume)

    result = []

    for job in match_jobs:
        analysis = ats_agent.analyze(resume,job)

        result.append({
            "job": job,
            "analysis": analysis
        }
        )

    return result


