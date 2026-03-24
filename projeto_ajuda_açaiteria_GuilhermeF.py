print("bem vindo ao sistema de ajuda da açaíteria! como posso ajudar?")
print("1 - Cardápio")
print("2 - Horário de funcionamento")
print("3 - Localização")
opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("\nNosso cardápio inclui:")
    print("- Açaí na tigela")
    print("- Açaí com frutas")
    print("- Açaí com granola")
    print("- Açaí com leite condensado\n")

elif opcao == "2":
    print("\nNosso horário de funcionamento é:")
    print("Segunda a sexta: 10h às 22h")
    print("Sábado: 10h às 23h")
    print("Domingo: 12h às 20h\n")

elif opcao == "3":
    print("\nNossa localização é:")
    print("Av. seila-aonde, 67 - São Paulo/SP")
    print("Rua sem-nome, 99 - São Paulo/SP")
    print("Rua escura, 24 - São Paulo/SP\n")

else:
    print("\nOpção inválida. Por favor, escolha uma opção válida.\n")