# analyzer.py

from skills_db import SKILL_DB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills(text):

    found_skills = []

    for skill in SKILL_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_similarity(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)

    score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return round(float(score[0][0]) * 100, 2)


def generate_suggestions(score, skills_found, job_description):

    suggestions = []

    if score < 40:
        suggestions.append("Low match score. Add more job-specific keywords.")

    elif score < 70:
        suggestions.append("Moderate match. Improve technical skill alignment.")

    else:
        suggestions.append("Strong match for the job role.")

    # Missing skills detection
    missing_skills = []
    for skill in SKILL_DB:
        if skill in job_description.lower() and skill not in skills_found:
            missing_skills.append(skill)

    if missing_skills:
        suggestions.append(f"Consider adding: {', '.join(missing_skills)}")

    return suggestions