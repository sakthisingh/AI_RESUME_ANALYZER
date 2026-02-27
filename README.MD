# AI Resume Analyzer

An intelligent resume screening tool that compares a resume with a target job description and gives clear, actionable feedback to improve ATS and recruiter alignment.

## Project Vision

AI Resume Analyzer is built to help candidates answer one important question before applying:

**"How well does my resume match this role, and what should I improve right now?"**

Instead of guessing, users get a measurable match score, detected skills, and targeted suggestions.

## What Problem This Solves

Most applicants face three common issues:

- They don't know if their resume matches the role requirements.
- They miss critical keywords used by ATS filters.
- They get no immediate feedback before submitting applications.

This project closes that gap with fast NLP-based analysis.

## Key Features

- Upload resume files in `PDF` or `DOCX`
- Paste any job description
- Extract and clean resume text
- Detect technical skills from a predefined skill database
- Calculate a resume-job match score using TF-IDF + cosine similarity
- Generate practical suggestions, including missing skill recommendations

## How It Works

1. User uploads a resume and enters a job description.
2. Resume text is extracted:
   - `pdfplumber` for PDF
   - `python-docx` for DOCX
3. Text is preprocessed:
   - lowercasing
   - punctuation cleanup
   - stopword removal (NLTK)
4. Skills are detected by matching terms from `SKILL_DB`.
5. Similarity score is computed with:
   - `TfidfVectorizer`
   - `cosine_similarity`
6. Suggestions are generated based on score bands and missing job-relevant skills.

## Scoring Logic

- `< 40`: Low alignment (major improvement needed)
- `40 - 69.99`: Moderate alignment (optimize keywords and skills)
- `>= 70`: Strong alignment (good fit signal)

## Tech Stack

- Python
- Streamlit
- scikit-learn
- NLTK
- pdfplumber
- python-docx

## Project Structure

```text
AI_RESUME_ANALYZER/
|-- app.py            # Streamlit UI and user flow
|-- analyzer.py       # Skill extraction, scoring, suggestions
|-- utils.py          # Resume parsing and text cleaning
|-- skills_db.py      # Skill keyword dataset
|-- requirements.txt  # Dependencies
|-- resumes/          # Uploaded resume storage
|-- README.md
```

## Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI_RESUME_ANALYZER
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Open Streamlit in your browser (usually `http://localhost:8501`).

## Example Output

After analysis, the app returns:

- **Match Score:** e.g., `72.35%`
- **Skills Found:** e.g., `python`, `sql`, `git`
- **Suggestions:** e.g., add missing skills such as `docker`, `aws`

## Current Limitations

- Skill matching is keyword-based (no semantic synonym expansion).
- Context depth is limited (does not evaluate quality of experience).
- Resume files are stored locally in `resumes/`.
- NLTK stopwords are downloaded at runtime.

## Future Improvements

- Add synonym-aware skill mapping and normalization
- Section-wise scoring (Skills, Projects, Experience)
- LLM-based resume rewrite recommendations
- ATS optimization checklist and keyword density report
- Downloadable report export (PDF/JSON)
- User accounts and cloud storage integration

## Contributions

Contributions are welcome. Good starting areas:

- Better parsing for complex PDF layouts
- Stronger skill extraction logic
- Test coverage for scoring and suggestions
- UI upgrades with analytics dashboards

## License

No license file is included yet. Add a `LICENSE` file (e.g., MIT) if you want public reuse rights to be clear.
