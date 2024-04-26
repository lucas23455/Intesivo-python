def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPor favor me diga seu nome')

    f_name = input('Primeiro nome:')
    l_name = input('Ultimo nome:')

    sair = input('desja continuar (s/n)')

    if sair == 'n':
        print('finalizando programa...')
        break



    formatted_name = get_formatted_name(f_name,l_name)
    print(f'\nOla {formatted_name}')