import nltk
import os
import re
import subprocess
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spacy.util import is_package

# 🔁 Add local nltk path if needed
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

# ✅ Ensure NLTK stopwords
try:
    STOPWORDS = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    STOPWORDS = set(stopwords.words("english"))

# ✅ Ensure spaCy model is installed
if not is_package("en_core_web_sm"):
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)

nlp = spacy.load("en_core_web_sm")

def load_skills(filepath="skills.txt"):
    with open(filepath, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def extract_skills(text, known_skills):
    text = text.lower()
    found_skills = []
    for skill in known_skills:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)
    return found_skills

def extract_new_skills(text, known_skills):
    doc = nlp(text)
    candidates = []
    for token in doc:
        if (
            token.is_alpha
            and token.text.lower() not in STOPWORDS
            and token.text.lower() not in known_skills
            and len(token.text) > 2
        ):
            candidates.append(token.text.lower())
    return sorted(set(candidates))
