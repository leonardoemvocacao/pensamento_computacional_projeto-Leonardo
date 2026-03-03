'''
CRUD

AÇAITERIA

DESCRIÇÃO

'''


print('\n === Sistema de Açaiteria === \n')

print ("1. cadastro dos clientes")
print ("2. cardapio da loja")
print ("3. pedidos")
print ("4. chat da loja de açai")
print ("5. ajuda")
print ("0. Sair")

while True:

    escolha_menu = input("\n Escolha uma opção: ")
    if escolha_menu == "1":

        print("Agendando cliente...")
        nome_cliente = input ("Digite o nome do cliente:")
        telefone_cliente = input ("Digite o telefone do cliente:")

    elif escolha_menu == "0":

        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")

'''

CRUD

sistema de agendamento de aulas - meet

'''
print("sistema de agendamento de aulas - meet")

id_usuario = input ("digite sua turma: (ex: A, B, C, D, ): ")


email_usuario - input("digite seu email: (nome.sobrenome@gmail.com) ")