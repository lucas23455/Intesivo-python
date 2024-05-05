
respostas = {}

active = True
while active:
    nome = input('\n Qual é seu nome ?')
    resposta = input('Qual montanha voce gostaria de escalar algum dia ?')

    respostas [nome] = resposta

    repeat = input('gostaria de deixar uma outra pessoa responder ? (s/n)')


    if repeat == 'n':
        active = False

    print('\tOs resultados')

    for nome, resposta in respostas.items():
        print(f'{nome} voce gostaria de escalar {resposta}')
