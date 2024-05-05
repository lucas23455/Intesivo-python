prompt = '\nPaises que visitou:'

prompt += '\ndigite "sair" para terminar o programa'


while True:
    city = input(prompt)

    if city == 'sair':
        print('encerrando o programa...')
        break

    else:
        print(f'Eu adoraria ir para {city.title()} !')