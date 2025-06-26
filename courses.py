import requests
from config import RAPIDAPI_KEY  # ✅ secure import

def get_top_youtube_courses(skill, max_results=2):
    url = "https://youtube-search-and-download.p.rapidapi.com/search"
    querystring = {
        "query": f"{skill} course for beginners",
        "type": "v",
        "sort": "r"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "youtube-search-and-download.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        data = response.json()
        results = data.get("contents", [])[:max_results]
        videos = []
        for item in results:
            video = item.get("video", {})
            if video:
                title = video.get("title")
                url = f"https://www.youtube.com/watch?v={video.get('videoId')}"
                videos.append((title, url))
        return videos
    except Exception as e:
        print(f"❌ YouTube API error: {e}")
        return []
