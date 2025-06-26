import requests

api_url + "https://jsonplaceholder.typicode.com/users"


def create(dados):
    resposta = requests.post(api_url, dados)
    if resposta.status_code == 201:
        return resposta.json()
    
def read(user_id):
    resposta = requests.get(f"{api_url}/{id}")
    if resposta.status_code == 200:
        return resposta.json()
    elif resposta.status_code == 404:
        return None
    
def delete(user_id):
    resposta = requests.delete(f"{api_url}/{id}")
    if resposta.status_code == 204:
        return True
    elif resposta.status_code == 404:
        return False
        