import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class ATSAgent:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

    def analyze(self, resume, job):

        prompt = f"""
You are an ATS system.

Evaluate resume against job description.

Return:

Match Score (0-100)

Strengths
Weaknesses
Important ATS Keywords
Missing Keywords
Suggestions to improve the resume

RESUME:
{resume}

JOB DESCRIPTION:
{job}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content