import requests

def lessons(tg_id:str):
    response = requests.post('http://127.0.0.1:3000/post/lessons', json={
        "userTelegramId": tg_id,
    })

    if response.status_code == 200:
        return response.json()

