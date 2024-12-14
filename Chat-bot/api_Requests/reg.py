import requests

def register(tg, name,group_uuid):

    response = requests.post('http://127.0.0.1:8002/register', json={
          "tg_id": tg,
          "name": name,
          "group_uuid": group_uuid})


    if response.status_code == 200:
        return True
