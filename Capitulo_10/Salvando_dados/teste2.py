import json

nome_arquivo = 'usuario.json'

with open(nome_arquivo) as arquivo:
    usuario = json.load(arquivo)
    print(f'bem vindo de volta {usuario}')