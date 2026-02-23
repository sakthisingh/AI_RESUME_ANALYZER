# AI Resume Analyzer

AI Resume Analyzer is a Python-based web application that analyzes a resume and compares it with a job description.

It calculates a match score, detects technical skills, and provides suggestions to improve the resume.

## What This Project Does

- Upload resume (`PDF` or `DOCX`)
- Extract text from the file
- Clean and preprocess text
- Detect technical skills
- Compare resume with job description
- Calculate match percentage
- Suggest improvements

## Technologies Used

- Python
- NLTK (text preprocessing)
- Scikit-learn (TF-IDF and cosine similarity)
- pdfplumber (PDF extraction)
- python-docx (DOCX extraction)
- Streamlit (web interface)

## Project Structure

```text
resume_analyzer/
+-- app.py              # Streamlit UI
+-- analyzer.py         # Skill extraction and scoring logic
+-- utils.py            # Text extraction and cleaning
+-- skills_db.py        # Skill database
+-- resumes/            # Temporary resume storage
+-- requirements.txt    # Required libraries
```

## How It Works

1. User uploads a resume.
2. Text is extracted from `PDF`/`DOCX`.
3. Text is cleaned (stopwords, symbols, etc.).
4. Skills are matched from the skill database.
5. TF-IDF + cosine similarity calculate the match score.
6. Suggestions are generated.

## Match Score Meaning

| Score Range | Result |
| --- | --- |
| 0–39% | Low match |
| 40–69% | Moderate match |
| 70–100% | Strong match |

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume_analyzer.git
cd resume_analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The application will open in your browser.

## Example

If a job description contains `Python`, `Machine Learning`, and `TensorFlow`:

- Resume with ML skills -> higher score
- Resume with unrelated skills (for example, Flutter only) -> lower score

The system primarily checks keyword similarity.

## Future Improvements

- Add experience detection
- Add education extraction
- Use BERT for better semantic matching
- Add database integration
- Deploy to cloud

## Author

**Sakthi Singh**  
Information Technology Student  
AI and Machine Learning Enthusiast
