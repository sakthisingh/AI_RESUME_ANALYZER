# app.py

import streamlit as st
import os
from utils import extract_text, clean_text
from analyzer import extract_skills, calculate_similarity, generate_suggestions

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description:

        # Save uploaded file temporarily
        file_path = os.path.join("resumes", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract and clean
        raw_text = extract_text(file_path)
        cleaned_text = clean_text(raw_text)

        # Analyze
        skills = extract_skills(cleaned_text)
        score = calculate_similarity(cleaned_text, job_description)
        suggestions = generate_suggestions(score, skills, job_description)

        # Output
        st.subheader("📊 Match Score")
        st.success(f"{score}%")

        st.subheader("🧠 Skills Found")
        st.write(skills)

        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.write("-", s)

    else:
        st.warning("Please upload resume and enter job description.")