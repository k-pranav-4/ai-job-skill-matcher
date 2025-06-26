import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Load stopwords once
STOPWORDS = set(stopwords.words("english"))

def load_skills(filepath="skills.txt"):
    """
    Load known skills from a text file.
    """
    with open(filepath, "r") as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    return skills

def extract_skills(text, known_skills):
    """
    Extract skills from text by comparing against known skills.
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
    Extract potential new skills using keyword heuristics.
    Avoids stopwords, short/common words, and known skills.
    """
    text = text.lower()
    tokens = word_tokenize(text)
    filtered = [
        word for word in tokens
        if word.isalpha() and
           word not in STOPWORDS and
           word not in known_skills and
           len(word) > 2
    ]
    return list(set(filtered))
