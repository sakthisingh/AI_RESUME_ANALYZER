🚀 AI Resume Analyzer
AI Resume Analyzer is a Python-based web application that analyzes a resume and compares it with a job description.
It calculates a match score, detects technical skills, and gives suggestions to improve the resume


What This Project Does
Upload resume (PDF or DOCX)
Extract text from the file
Clean and preprocess text
Detect technical skills
Compare resume with job description
Calculate match percentage
Suggest improvements

...
Technologies Used

Python

NLTK (Text preprocessing)

Scikit-learn (TF-IDF & Cosine Similarity)

pdfplumber (PDF extraction)

python-docx (DOCX extraction)

Streamlit (Web interface)
...

...
PROJECT FOLDER STRUCTURE:
resume_analyzer/
│
├── app.py              # Streamlit UI
├── analyzer.py         # Skill extraction & scoring logic
├── utils.py            # Text extraction & cleaning
├── skills_db.py        # Skill database
├── resumes/            # Temporary resume storage
├── requirements.txt    # Required libraries
...

...
How It Works
User uploads resume
Text is extracted from PDF/DOCX
Text is cleaned (remove stopwords, symbols, etc.)
Skills are matched from skill database
TF-IDF + Cosine Similarity calculate match score
Suggestions are generated
...

...
MATCH SCORE MEANING 
| Score   | Result         |
| ------- | -------------- |
| 0–39%   | Low match      |
| 40–69%  | Moderate match |
| 70–100% | Strong match   |
...




👨‍💻 Author

Sakthi Singh
Information Technology Student
AI & Machine Learning Enthusiast
