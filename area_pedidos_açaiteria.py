print("Olá cliente, seja bem-vindo à nossa açaíteria, aqui você pode montar seu próprio açaí do jeito que quiser, vamos começar?")
print("Vou agendar seu pedido, qual seu nome?")
nome = input()
print(f"{nome}, qual o número do pedido?")
numero_pedido = input()
print(f"Ok {nome}, seu pedido de número {numero_pedido} foi agendado. Agora vamos montar seu açaí. Qual o sabor do açaí que você deseja?")
sabor = input()

sabores_disponiveis = [
    'açaí tradicional',
    'açaí com banana',
    'açaí com morango',
    'açaí com guaraná',
    'açaí zero açúcar',
    'açaí com leite condensado'
]

frutas_disponiveis = [
    'banana',
    'morango',
    'kiwi',
    'abacaxi',
    'manga',
    'coco',
    'uva'
]


doces_e_guloseimas_disponiveis = [
    'leite condensado',
    'leite em pó',
    'chocolate granulado',
    'confeito (tipo M&Ms)',
    'calda de chocolate',
    'brigadeiro',
    'nutella',
    'chocolate picadinho',
    'beijinho',
]



crocantes_disponiveis = [
    'granola',
    'amendoim',
    'castanha',
    'aveia',
    'sucrilhos',
    'bis',
    'oreo',
    'ovo maltine',
]


tamanhos_disponiveis = [
    '300ml',
    '500ml',
    '700ml',
    '1 litro',
    '1,5 litro',
    '2 litros'
]
# Escolha do sabor
print("\nSabores disponíveis:")
for i, sabor in enumerate(sabores_disponiveis, start=1):
    print(f"{i}. {sabor}")

opcao_sabor = int(input("Digite o número do sabor desejado: "))
sabor_escolhido = sabores_disponiveis[opcao_sabor - 1]

# Escolha da fruta
print("\nFrutas disponíveis:")
for i, fruta in enumerate(frutas_disponiveis, start=1):
    print(f"{i}. {fruta}")

opcao_fruta = int(input("Digite o número da fruta desejada: "))
fruta_escolhida = frutas_disponiveis[opcao_fruta - 1]

# Escolha do tamanho
print("\nTamanhos disponíveis:")
for i, tamanho in enumerate(tamanhos_disponiveis, start=1):
    print(f"{i}. {tamanho}")

opcao_tamanho = int(input("Digite o número do tamanho desejado: "))
tamanho_escolhido = tamanhos_disponiveis[opcao_tamanho - 1]

# Resumo do pedido
print("\nResumo do pedido:")
print(f"Cliente: {nome}")
print(f"Número do pedido: {numero_pedido}")
print(f"Sabor: {sabor_escolhido}")
print(f"Fruta: {fruta_escolhida}")
print(f"Tamanho: {tamanho_escolhido}")
print("Seu açaí está sendo preparado! Obrigado pela preferência.")

print("valor do pedido: R$ 80,00")