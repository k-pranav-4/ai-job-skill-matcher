import streamlit as st
import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from utils import load_skills, extract_skills
from courses import get_top_youtube_courses
from job_api import get_job_suggestions

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

st.set_page_config(page_title="AI Job Skill Matcher", layout="centered")

st.title("🧠 AI Job Skill Matcher")
st.markdown("Upload your **PDF resume**, paste a **Job Description**, and find your matching skills, fit score, and curated learning resources!")

SKILL_FILE = "skills.txt"

def extract_text_from_pdf_file(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def add_new_skills(jd_text, known_skills, extracted_skills):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', jd_text.lower())
    new_candidates = set(words) - set(known_skills)
    filtered = []

    for word in new_candidates:
        if (
            word not in extracted_skills
            and word not in stop_words
            and word.isalpha()
            and len(word) > 3
            and len(word.split()) <= 2
        ):
            filtered.append(word)

    if filtered:
        with open(SKILL_FILE, "a") as f:
            for skill in filtered:
                f.write(f"{skill}\n")
        st.info(f"🧩 {len(filtered)} new potential skills added to skills.txt: {', '.join(filtered[:5])}...")
        return True
    return False

# Upload resume
resume_file = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])
jd_input = st.text_area("💼 Paste Job Description", height=200)

if st.button("🔍 Analyze"):
    if resume_file is None or not jd_input.strip():
        st.warning("Please upload a resume and paste the job description.")
    else:
        resume_text = extract_text_from_pdf_file(resume_file)

        known_skills = load_skills()
        jd_skills = extract_skills(jd_input, known_skills)
        resume_skills = extract_skills(resume_text, known_skills)

        matched = set(jd_skills) & set(resume_skills)
        missing = set(jd_skills) - set(resume_skills)
        match_percentage = (len(matched) / len(jd_skills) * 100) if jd_skills else 0

        # ✨ Auto-update skills.txt
        # newly_added = add_new_skills(jd_input, known_skills, jd_skills)

        st.subheader("✅ Matched Skills")
        st.write(", ".join(matched) if matched else "No skills matched.")

        st.subheader("❌ Missing Skills (from JD)")
        st.write(", ".join(missing) if missing else "None! You're a perfect match. 🚀")

        st.subheader("📊 Match Score")
        st.metric(label="Skill Match", value=f"{match_percentage:.2f} %")

        # Pie chart
        st.subheader("🥧 Skill Match Breakdown")
        labels = ['Matched', 'Missing']
        sizes = [len(matched), len(missing)]
        colors = ['#4CAF50', '#FF5252']
        explode = (0.05, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', startangle=90, textprops={'color': "white"})
        ax.axis('equal')
        st.pyplot(fig)

        st.subheader("💼 Current Job Openings That Matches With Your Skills")
        if resume_skills:
            jobs = get_job_suggestions(resume_skills, location="India", results=5)
            if jobs:
                for job in jobs:
                    st.markdown(f"- **{job['title']}** at *{job['company']}* — {job['location']}  \n  🔗 [View Job Posting]({job['link']})")
            else:
                st.info("No matching jobs found this week.")
        else:
            st.warning("No skills found in resume to suggest jobs.")

        st.subheader("📚 Suggested Resources to Learn")
        for skill in missing:
            st.markdown(f"### 🛠️ {skill.title()}")
            yt_courses = get_top_youtube_courses(skill)
            if yt_courses:
                st.markdown("**▶️ YouTube Courses:**")
                for title, url in yt_courses:
                    st.markdown(f"- 🔗 [{title}]({url})")
            else:
                st.warning(f"No courses found for {skill}")
