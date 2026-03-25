# =========================
# SISTEMA AÇAITÉRIA 🍧
# =========================

clientes = []

# =========================
# CADASTRO - Por Wilson
# =========================
def cadastro():
    while True:
        print("\n--- CADASTRO DE CLIENTES ---")
        print("1 - Cadastrar cliente")
        print("2 - Ver clientes")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")

            clientes.append({
                "nome": nome,
                "telefone": telefone,
                "email": email
            })

            print("✅ Cliente cadastrado com sucesso!")

        elif opcao == "2":
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for i, c in enumerate(clientes, start=1):
                    print(f"\nCliente {i}")
                    print("Nome:", c["nome"])
                    print("Telefone:", c["telefone"])
                    print("Email:", c["email"])

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")


# =========================
# CARDÁPIO - Por Gustavo
# =========================
def cardapio():
    pedido = []
    total = 0

    while True:
        print("\n--- CARDÁPIO ---")
        print("1 - Açaí pequeno - R$15")
        print("2 - Açaí médio - R$19")
        print("3 - Açaí grande - R$25")
        print("4 - Suco - R$7")
        print("5 - Finalizar pedido")
        print("0 - Cancelar")

        opcao = input("Escolha: ")

        if opcao in ["1", "2", "3", "4"]:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade <= 0:
                    print("Digite um número válido!")
                    continue
            except ValueError:
                print("Digite apenas números!")
                continue

            if opcao == "1":
                pedido.append(f"{quantidade}x Açaí pequeno")
                total += 15 * quantidade
            elif opcao == "2":
                pedido.append(f"{quantidade}x Açaí médio")
                total += 19 * quantidade
            elif opcao == "3":
                pedido.append(f"{quantidade}x Açaí grande")
                total += 25 * quantidade
            elif opcao == "4":
                pedido.append(f"{quantidade}x Suco")
                total += 7 * quantidade

            print("✅ Item adicionado!")

        elif opcao == "5":
            print("\n--- RESUMO ---")
            if not pedido:
                print("Nenhum item no pedido.")
            else:
                for item in pedido:
                    print("-", item)
                print(f"Total: R${total:.2f}")
            break

        elif opcao == "0":
            print("Pedido cancelado.")
            break

        else:
            print("Opção inválida!")


# =========================
# PEDIDO PERSONALIZADO - Por Rhuan
# =========================
def pedido_personalizado():
    print("\n--- MONTAR AÇAÍ ---")

    nome = input("Seu nome: ")
    numero_pedido = input("Número do pedido: ")

    sabores = ['tradicional', 'banana', 'morango', 'guaraná', 'zero açúcar']
    frutas = ['banana', 'morango', 'kiwi', 'abacaxi']
    tamanhos = ['300ml', '500ml', '700ml']

    try:
        print("\nSabores:")
        for i, s in enumerate(sabores, 1):
            print(f"{i} - {s}")
        sabor = sabores[int(input("Escolha: ")) - 1]

        print("\nFrutas:")
        for i, f in enumerate(frutas, 1):
            print(f"{i} - {f}")
        fruta = frutas[int(input("Escolha: ")) - 1]

        print("\nTamanhos:")
        for i, t in enumerate(tamanhos, 1):
            print(f"{i} - {t}")
        tamanho = tamanhos[int(input("Escolha: ")) - 1]

    except (ValueError, IndexError):
        print("Entrada inválida!")
        return

    print("\n--- RESUMO ---")
    print("Cliente:", nome)
    print("Pedido:", numero_pedido)
    print("Sabor:", sabor)
    print("Fruta:", fruta)
    print("Tamanho:", tamanho)
    print("Pedido em preparo! 🍧")


# =========================
# CHAT - Por Leonardo
# =========================
def chat():
    estado = "inicio"

    while True:
        print("\n--- CHAT ---")
        msg = input("Você: ").lower()

        if msg == "sair":
            print("Atendimento encerrado.")
            break

        if estado == "inicio":
            if msg == "oi":
                print("Olá! Digite 'cardapio' ou 'pedido'")
            elif msg == "cardapio":
                print("Temos: pequeno, médio e grande")
            elif msg == "pedido":
                print("Qual tamanho?")
                estado = "tamanho"
            else:
                print("Digite 'oi', 'cardapio' ou 'pedido'")

        elif estado == "tamanho":
            if msg in ["pequeno", "medio", "médio", "grande"]:
                print(f"Pedido de açaí {msg} confirmado! 🍧")
                estado = "inicio"
            else:
                print("Escolha: pequeno, médio ou grande")


# =========================
# AJUDA - Guilherme Firmino
# =========================
def ajuda():
    print("\n--- AJUDA ---")
    print("1 - Cardápio")
    print("2 - Horário")
    print("3 - Localização")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Açaí, frutas, granola, leite condensado")
    elif opcao == "2":
        print("Seg a Sex: 10h às 22h")
    elif opcao == "3":
        print("São Paulo - SP")
    else:
        print("Opção inválida")


# =========================
# MENU PRINCIPAL
# =========================
def main():
    while True:
        print("\n===== AÇAITÉRIA =====")
        print("1 - Cadastro")
        print("2 - Cardápio")
        print("3 - Montar Açaí")
        print("4 - Chat")
        print("5 - Ajuda")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            cardapio()
        elif opcao == "3":
            pedido_personalizado()
        elif opcao == "4":
            chat()
        elif opcao == "5":
            ajuda()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")


# EXECUTAR SISTEMA
main()