import json


def nome_armazenado():
    nome_arquivo = 'usuario.json'

    try:
        with open(nome_arquivo) as arquivo:
            usuario = json.load(arquivo)

    except FileNotFoundError:
        return None
    else:
        return usuario


def saudaçao():
    usuario = nome_armazenado()
    if usuario:
        print(f'Bem vindo de volta {usuario}')

    else:
        nome_arquivo = 'usuario.json'
        usuario = input('qual é seu nome?')
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(usuario, arquivo)
            print(f'Nos lembraremos de voce quando voce volta {usuario}')


saudaçao()