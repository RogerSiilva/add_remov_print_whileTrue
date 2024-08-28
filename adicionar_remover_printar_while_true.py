lista_de_compras = []

while True:
    print()

    print('1 Adicionar item')
    print('2 Remover item')
    print('3 Ver lista')
    print('4 Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        item = input('Digite um item: ')
        lista_de_compras.append(item)
    elif escolha == '2':
        item = input('Remover item: ')
        lista_de_compras.remove(item)
    elif escolha == '3':
        print(lista_de_compras)
    elif escolha == '4':
        break



