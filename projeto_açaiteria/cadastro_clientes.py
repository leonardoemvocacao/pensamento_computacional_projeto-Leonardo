clientes = []

while True:
    print("\n--- Açaitéria ---")
    print("1 - Cadastrar cliente")
    print("2 - Ver clientes")
    print("0 - sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        cliente = [nome, telefone, email]
        clientes.append(cliente)

        print("Cliente cadastrado com sucesso")

    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for i in range(len(clientes)):
                print("\nCliente", i)
                print("Nome:", clientes[i][0])
                print("Telefone:", clientes[i][1])
                print("Email:", clientes[i][2])

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")