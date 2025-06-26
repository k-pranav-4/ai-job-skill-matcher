
# 🧠 AI Job Skill Matcher

An intelligent web app that helps users analyze job descriptions and their resumes to:
- Extract and compare required skills
- Visualize match percentage
- Suggest learning resources (YouTube)
- Recommend currently open jobs (via API)

Built with **Python**, **Streamlit**, **spaCy**, and **RapidAPI**.

---

## 🚀 Features

- 📄 **Upload Resume (PDF)**
- 💼 **Paste Job Description**
- 🔍 Extract skills using NLP
- 📊 Visual match score with pie chart
- 📚 Suggested YouTube courses for missing skills
- 💼 Live job openings from RapidAPI's job search
- 🛠 Modular, clean code with utility scripts

---

## 📸 Screenshots

| Resume Analysis | Skill Suggestions |
|------------------|-------------------|
| ![](https://lnk.ink/demo_1) | ![](https://lnk.ink/demo_2) |

---

## 📁 Project Structure

```
job_skill_matcher/
├── app.py                      # Main Streamlit app
├── config.py                   # 🔒 Your API key (excluded via .gitignore)
├── courses.py                  # YouTube course fetch logic
├── job_api.py                  # Job matching via RapidAPI (jSearch)
├── skills.txt                  # Known skills list
├── utils.py                    # Skill extraction functions
├── requirements.txt            # Python dependencies
├── test_*.py                   # Testing scripts
└── ...
```

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/job_skill_matcher.git
cd job_skill_matcher

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a file named `config.py`:

```python
# config.py
RAPIDAPI_KEY = "your_actual_rapidapi_key_here"
```

Add it to `.gitignore` to avoid exposing secrets.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## ☁️ Deployment

This app can be deployed via:
- [✅ Streamlit Cloud](https://streamlit.io/cloud) – easiest & free
- [🚀 Render](https://render.com) or [Railway](https://railway.app) – for custom domains
- [💻 VPS/Cloud] (optional, advanced)

---

## ✨ Future Enhancements

- Add login + saved progress
- Suggest courses from Coursera & Udemy
- Export PDF reports
- Resume parsing with named entity recognition (NER)

---

## 🙏 Credits

- [spaCy](https://spacy.io/)
- [Streamlit](https://streamlit.io/)
- [RapidAPI](https://rapidapi.com/)
- YouTube Search API, JSearch API

---

## 📃 License

[MIT](LICENSE)
