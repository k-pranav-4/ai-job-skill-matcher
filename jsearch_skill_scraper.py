import requests
import re
from bs4 import BeautifulSoup

from config import RAPIDAPI_KEY

def extract_keywords(text):
    text = BeautifulSoup(text, "html.parser").get_text().lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    skill_keywords = [
        "python", "c++", "slam", "ros", "tensorflow", "pytorch", "opencv", "git",
        "linux", "docker", "azure", "aws", "machine learning", "deep learning",
        "matlab", "nlp", "data analysis", "object detection", "path planning",
        "visual studio", "gitlab", "ci/cd", "simd", "kubernetes", "cad", "sensor fusion"
    ]

    found = []
    for skill in skill_keywords:
        pattern = rf'\b{re.escape(skill)}\b'
        if re.search(pattern, text):
            found.append(skill)

    return sorted(set(found))

def fetch_job_descriptions(title, num_results=5):
    print("📡 Fetching job descriptions...")
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": title,
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        jobs = data.get("data", [])

        # Uncomment below to debug response
        print("📦 Raw API Response Preview:", jobs[:1])

        return [job.get("job_description", "") for job in jobs if "job_description" in job]
    except Exception as e:
        print("❌ API error:", e)
        return []

def save_skills_to_file(skills, filename="skills.txt"):
    if not skills:
        print("\n⚠️ No skills found.")
        return

    print(f"\n✨ Extracted {len(skills)} unique skills:\n")
    print(", ".join(skills))

    with open(filename, "a") as f:
        for skill in skills:
            f.write(skill + "\n")

    print("✅ Skills added to skills.txt")

if __name__ == "__main__":
    title = input("🔍 Enter job title (e.g., robotics engineer): ").strip()
    descriptions = fetch_job_descriptions(title)
    all_skills = set()
    for desc in descriptions:
        skills = extract_keywords(desc)
        all_skills.update(skills)

    save_skills_to_file(sorted(all_skills))
