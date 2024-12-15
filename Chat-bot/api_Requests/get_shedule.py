import requests

def shedule(group:str):
    url = f'http://127.0.0.1:8002/get_shedule?group_uuid={group}'
    response = requests.get(url)

    if response.status_code == 200:

        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None


