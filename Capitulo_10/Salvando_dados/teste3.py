import json

nome_arquivo = 'usuario.json'

try:
    with open(nome_arquivo) as arquivo:
        usuario = json.load(arquivo)
except FileNotFoundError:
    usuario = input('Qual é seu nome? ')
    with open(nome_arquivo,'w') as arquivo:
        json.dump(usuario, arquivo)
        print(f'Nos lembraremos de você quando voltar, {usuario}!')
else:
    print(f'Bem-vindo de volta, {usuario}!')
