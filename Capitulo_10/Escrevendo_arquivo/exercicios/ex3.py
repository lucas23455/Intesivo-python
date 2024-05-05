nome_arquivo = 'respostas.txt'

while True:
    resposta = input('porque voce gosta de programaçao (ou "sair" para finalizar)')

    if resposta.lower() == 'sair':
        print('encerrando o programa...')
        break

    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(resposta + '\n')

print('Obrigado pela respostas!!')