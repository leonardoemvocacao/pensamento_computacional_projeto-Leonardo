estado = "inicio"

while True:
    print("\n--- CHAT DA AÇAITÉRIA ---")
    mensagem = input("Cliente: ").lower()

    if mensagem == "sair":
        print("Loja: Atendimento encerrado!")
        break

    if estado == "inicio":
        if mensagem == "oi":
            print("Loja: Olá! Bem-vindo à açaiteria 🍧")
            print("Loja: Digite 'cardapio' para ver as opções")
        
        elif mensagem == "cardapio":
            print("Loja: Temos açaí nos tamanhos:")
            print("- Pequeno")
            print("- Médio")
            print("- Grande")
            print("Loja: Digite 'pedido' para fazer um pedido")
        
        elif mensagem == "pedido":
            print("Loja: Qual tamanho você deseja?")
            estado = "escolhendo"
        
        else:
            print("Loja: Pode digitar 'oi', 'cardapio' ou 'pedido' 😊")

    elif estado == "escolhendo":
        if mensagem in ["pequeno", "medio", "médio", "grande"]:
            print(f"Loja: Perfeito! Um açaí {mensagem} 🍧")
            print("Loja: Vou encaminhar seu pedido!")
            estado = "inicio"
        else:
            print("Loja: Escolha entre pequeno, médio ou grande 😊")
           
            print("finalizar pedido")