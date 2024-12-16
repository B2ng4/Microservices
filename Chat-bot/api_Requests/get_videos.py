import requests

def video_urls(discipline:str):
    url = f'http://127.0.0.1:8006/get_video_urls?discipline={discipline}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None


print(video_urls("Матанализ"))