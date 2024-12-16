from googleapiclient.discovery import build


def search_videos_by_discipline( discipline: str, max_results: int = 10, api_key:str = "AIzaSyBx-b8iX0MmhRjt8aZ6VDVIuceBIqWlrdI"):

    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=f"полный курс по {discipline}",
        part="snippet",
        maxResults=max_results,
        type="video"
    )
    response = request.execute()

    video_links = [
        "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
        for item in response.get("items", [])
    ]

    return video_links[:3]






