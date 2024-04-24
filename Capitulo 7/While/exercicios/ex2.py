
while True:
    idade = input('Quantos anos vc tem ? (aperte "quit" para sair)')

    if idade.lower() == 'quit':
        print('encerrando o programa')
        break

    idade = int(idade)

    if idade <= 3:
        print('O ingresso é gratuito')

    elif idade <= 12:
        print('O ingresso é 10 dolares')

    else:
        print('O ingresso é 15 dolares')

