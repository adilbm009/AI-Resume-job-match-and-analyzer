import streamlit as st
from main import run_pipeline


st.title("AI Resume ATS Analyzer")


resume = st.text_area(
    "Paste your resume text"
)

if st.button("Analyze Resume"):

    with st.spinner("Analyzing..."):

        results = run_pipeline(resume)

    for r in results:

        st.subheader("Matched Job")

        st.write(r["job"])

        st.subheader("ATS Analysis")

        st.write(r["analysis"])

        st.divider()