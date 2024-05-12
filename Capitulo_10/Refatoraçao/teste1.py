import json

def saudaçao():
    nome_arquivo = 'usuario.json'

    try:
        with open(nome_arquivo) as arquivo:
            usuario = json.load(arquivo)

    except FileNotFoundError:
        usuario = input('qual é seu nome?')
        with open(nome_arquivo,'w') as arquivo:
            json.dump(usuario,arquivo)
            print(f'Nos lembraremos de voce quando voce volta {usuario}')

    else:
        print(f'bem vindo de volta {usuario}')


saudaçao()        