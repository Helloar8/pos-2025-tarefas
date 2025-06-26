import users 

opcao = input( "Digite c para criar, r para ler, d para deletar: " )
if opcao == "c":
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    dados = {"nome": nome, "email": email}
    usuario = users.create(dados)
    print(f"Usuário criado: {usuario}")

elif opcao == "r":
    user_id = int(input("Digite o ID do usuário: "))
    usuario = users.read(user_id)
    if usuario:
        print(f"Usuário encontrado: {usuario}")
    else:
        print("Usuário não encontrado.")

elif opcao == "d":
    user_id = int(input("Digite o ID do usuário a ser deletado: "))
    sucesso = users.delete(user_id)
    if sucesso:
        print("Usuário deletado com sucesso.")
    else:
        print("Usuário não encontrado ou não foi possível deletar.")
else:
    print("Opção inválida.")