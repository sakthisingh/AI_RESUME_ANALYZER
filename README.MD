AI Resume Analyzer

AI Resume Analyzer is a Python-based web application that analyzes a resume and compares it with a job description.

It calculates a match score, detects technical skills, and gives suggestions to improve the resume.

📌 What This Project Does

Upload resume (PDF or DOCX)

Extract text from the file

Clean and preprocess text

Detect technical skills

Compare resume with job description

Calculate match percentage

Suggest improvements

🛠 Technologies Used

Python

NLTK (Text preprocessing)

Scikit-learn (TF-IDF & Cosine Similarity)

pdfplumber (PDF extraction)

python-docx (DOCX extraction)

Streamlit (Web interface)

📂 Project Structure
resume_analyzer/
│
├── app.py              # Streamlit UI
├── analyzer.py         # Skill extraction & scoring logic
├── utils.py            # Text extraction & cleaning
├── skills_db.py        # Skill database
├── resumes/            # Temporary resume storage
├── requirements.txt    # Required libraries
🧠 How It Works

User uploads resume

Text is extracted from PDF/DOCX

Text is cleaned (remove stopwords, symbols, etc.)

Skills are matched from skill database

TF-IDF + Cosine Similarity calculate match score

Suggestions are generated

📊 Match Score Meaning
Score	Result
0–39%	Low match
40–69%	Moderate match
70–100%	Strong match
⚙️ How To Run The Project
Step 1: Clone the repository
git clone https://github.com/yourusername/resume_analyzer.git
cd resume_analyzer
Step 2: Install dependencies
pip install -r requirements.txt
Step 3: Run the app
streamlit run app.py

The application will open in your browser.

💡 Example

If Job Description contains:

Python, Machine Learning, TensorFlow

Resume with ML skills → High score

Resume with Flutter skills → Low score

Because the system checks keyword similarity.

🚀 Future Improvements

Add experience detection

Add education extraction

Use BERT for better semantic matching

Add database integration

Deploy on cloud

👨‍💻 Author

Sakthi Singh
Information Technology Student
AI & Machine Learning Enthusiast

This version is:

✔ Simple
✔ Clean
✔ Easy to read
✔ Suitable for GitHub
✔ Good for recruiters

If you want, I can now help you write a short 2–3 line project description for your GitHub repository title section.