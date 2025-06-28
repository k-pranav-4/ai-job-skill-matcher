import os
import re
import nltk
import spacy
from nltk.corpus import stopwords

# Set NLTK path and load stopwords
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))
STOPWORDS = set(stopwords.words("english"))

# ✅ Load spaCy model (must be preinstalled from requirements.txt)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError("❌ spaCy model not found. Make sure it is included in requirements.txt.")

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
    candidates = [
        token.text.lower()
        for token in doc
        if token.is_alpha and
           token.text.lower() not in STOPWORDS and
           token.text.lower() not in known_skills and
           len(token.text) > 2
    ]
    return sorted(set(candidates))
