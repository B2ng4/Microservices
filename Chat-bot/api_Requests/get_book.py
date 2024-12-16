import requests

def book(name_book:str):
    url = f'http://127.0.0.1:8005/get/book/{name_book}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None


