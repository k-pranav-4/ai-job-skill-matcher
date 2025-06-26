import requests
import streamlit as st
RAPIDAPI_KEY = st.secrets["RAPIDAPI_KEY"]


def get_job_suggestions(skills, location="India", results=5):
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    job_keywords = ", ".join(skills[:5])  # limit to top 5 skills
    query = {
        "query": job_keywords,
        "location": location,
        "page": "1",
        "num_pages": "1"
    }

    try:
        response = requests.get(url, headers=headers, params=query, timeout=10)
        data = response.json()

        jobs = []
        for job in data.get("data", [])[:results]:
            jobs.append({
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city") or location,
                "link": job.get("job_apply_link")
            })

        return jobs

    except Exception as e:
        print("❌ Job API Error:", e)
        return []
