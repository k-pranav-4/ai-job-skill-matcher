import os
import re
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ✅ Ensure local nltk stopwords work
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))
STOPWORDS = set(stopwords.words("english"))

# ✅ Auto-download spaCy model if missing
from spacy.util import is_package
import subprocess

if not is_package("en_core_web_sm"):
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

nlp = spacy.load("en_core_web_sm")

def load_skills(filepath="skills.txt"):
    """
    Load known skills from a text file.
    """
    with open(filepath, "r") as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    return skills

def extract_skills(text, known_skills):
    """
    Extract known skills from text using regex word boundary.
    """
    text = text.lower()
    found_skills = []
    for skill in known_skills:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)
    return found_skills

def extract_new_skills(text, known_skills):
    """
    Extract potential new skill-like keywords using spaCy NLP.
    Filters out stopwords, punctuation, digits, and known/common words.
    """
    text = text.lower()
    doc = nlp(text)

    new_skills = set()

    for token in doc:
        if (
            token.is_alpha and
            token.text not in STOPWORDS and
            token.text not in known_skills and
            len(token.text) > 2
        ):
            new_skills.add(token.text)

    return sorted(new_skills)
