# 🧠 AI Job Skill Matcher

A smart web tool that helps users analyze how well their resume matches a job description and suggests personalized learning resources and job opportunities.

🚀 **Live App**: [ai-job-skill-matcher-for-you.streamlit.app](https://ai-job-skill-matcher-for-you.streamlit.app/)

---

## 📌 Features

✅ Upload your **resume (PDF)** and paste a **job description** 
✅ Extract key skills from both resume and JD using NLP 
✅ Show **skill match percentage** and **pie chart visualization** 
✅ Recommend **YouTube learning resources** for missing skills 
✅ Fetch **real-time job openings** relevant to your resume skills 
✅ Secure API integration via Streamlit Secrets Manager (.streamlit/secrets.toml) for deployment. 
   (For local development, a config.py (excluded from GitHub) can be used.)

---

## 📁 Folder Structure

```
job_skill_matcher/
│
├── app.py                     # 🚀 Main Streamlit app
├── utils.py                   # ⚙️ Skill extraction logic
├── courses.py                 # ▶️ YouTube course API integration
├── job_api.py                 # 🧭 Job suggestions via API
├── skills.txt                 # 📋 Known skills
├── requirements.txt           # 📦 Python dependencies
├── nltk_data/                 # 🧠 Local NLTK stopwords
├── nltk_setup.py              # 📥 NLTK downloader (for local use)
├── .streamlit/
│   └── secrets.toml           # 🔐 Secure API keys (for Streamlit Cloud)
├── README.md                  # 📖 Project overview
├── .gitignore                 # 🚫 Excludes sensitive files and folders
└── (test scripts and other utils...)

```

---

## 🔧 Installation (For Local Use)

```bash
git clone https://github.com/k-pranav-4/ai-job-skill-matcher.git
cd ai-job-skill-matcher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python nltk_setup.py
streamlit run app.py
```

---

## 🧪 Example Use Case

- Upload a resume PDF 
- Paste a job description (e.g., for "Data Scientist") 
- The app:
  - Shows matched/missing skills
  - Displays a match score
  - Suggests YouTube videos to learn missing skills
  - Fetches current job listings based on your resume skills

---

## 🔐 Environment & Deployment

- Hosted on: [Streamlit Cloud](https://streamlit.io/cloud)
- The API key is stored securely using Streamlit Secrets Manager (.streamlit/secrets.toml) during deployment. 

---

## 🪪 License

MIT License © 2025 [Pranav (k-pranav-4)](https://github.com/k-pranav-4)
