def inicio():
    import os
    os.system("cls || clear")
    lista = []
    try:
        config = open('config.json', 'r', encoding='utf-8')
        config.close()
    except FileNotFoundError:
        config = open('config.json', 'w')
        config.write('Tutorial_Done=1')
        config.close()
        input("Avaliação Continuada 1 – Análise exploratória dos dados.\n\nCertifique-se que tenha as bibliotecas necessárias instaladas\nAs bibliotecas podem ser instaladas rodando o arquivo 'setup.py'\nEssa mensagem só será mostrada uma vez\n\nPressione ENTER para prosseguir")
    
    os.system("cls || clear")
    elementos = int(input("Insira a quantidade de elementos da lista: "))
    os.system("cls || clear")
    print("Insira os números a serem analisados: ")
    for i in range(elementos):
        x = int(input())
        lista.append(x)
    os.system("cls || clear")
    print(lista)
    return lista