nome_arquivo = 'guest.txt'

with open(nome_arquivo, 'w') as arquivo:
    while True:
        nome = input('Qual é o seu nome? ')
        arquivo.write(nome + '\n')

        response = input('Quer continuar? (s/n): ')

        while response.lower() != 's' and response.lower() != 'n':  # Loop até que a resposta seja válida
            print('Resposta incorreta')
            response = input('Responda (s/n): ')

        if response.lower() == 'n':
            print('Finalizando o programa!!')
            break

print('Os nomes foram registrados no arquivo!!')
