print('Me de dois numeros, e depois os divida')
print('aperte "s" para sair')

while True:
    primeiro_num = int(input('primeiro numero:'))

    if primeiro_num == 's':
        print('Encerrando o programa...')
        break

    segundo_num = int(input('segundo numero:'))

    if segundo_num == 's':
        print('encerrando o programa...')

    try:
        resultado =  primeiro_num/segundo_num
    except ZeroDivisionError:
        print('Voce não pode dividir por zero!!')
    else:
        print(resultado)