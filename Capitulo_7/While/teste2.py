prompt = '\nDida algo:'

prompt += '\ndigite "sair" para terminar o programa'

menssagem = ''

while menssagem != 'sair':
    menssagem = input(prompt)

    if menssagem != 'sair':
        print(menssagem)
