import requests
from getpass import getpass
from tabulate import tabulate

api_url = "https://suap.ifrn.edu.br/api/"

user = input("Insira sua matricula: ")
password = getpass("Insira sua senha: ")

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)




if response.status_code == 200:
    # Autenticação bem-sucedida
    print("✅ Autenticação bem-sucedida!")
    token = response.json().get('access')  # Obtém o token de acesso
    headers = {
        "Authorization": f'Bearer {token}'
    }
else:
   
    print("❌ Erro na autenticação! Verifique suas credenciais.")
    print(f"Detalhes do erro: {response.text}")
    exit() 

ano = input("Insira o ano para consulta do boletim: ")

# Faz a requisição para obter o boletim
print("📄 Obtendo boletim...")
response = requests.get(api_url + f"ensino/meu-boletim/{ano}/1/", headers=headers)

if response.status_code == 200:
    # Exibe o boletim formatado
    disciplinas = response.json()
    print("📚 Boletim obtido com sucesso!")


 # Formata o boletim em uma tabela

tabela_dados = []
for disciplina in disciplinas['results']:

    if disciplina['segundo_semestre'] == False:
        linha = [
            disciplina['disciplina'],
            disciplina['nota_etapa_1']['nota'],
            disciplina['nota_etapa_2']['nota'],
            disciplina['nota_etapa_3']['nota'],
            disciplina['nota_etapa_4']['nota']
        ]
    else:
        linha = [
            disciplina['disciplina'],
            "",
            "",
            disciplina['nota_etapa_1']['nota'],
            disciplina['nota_etapa_2']['nota']
        ]

    #add a linha na tebela
    tabela_dados.append(linha)

# Define cabeçalhos
cabecalhos = ["Disciplina", "Etapa 1", "Etapa 2", "Etapa 3", "Etapa 4"]


# Exibir a tabela formatada
print("\nBOLETIM - NOTAS POR ETAPA")
print(tabulate(tabela_dados, headers=cabecalhos, tablefmt="grid"))
    
