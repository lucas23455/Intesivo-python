import json

usuario = input('qual é seu nome?')

nome_arquivo = 'usuario.json'
with open(nome_arquivo, 'w') as arquivo:
    json.dump(usuario,arquivo)
    print(f'Nos lembraremos de voce quando voce voltar: {usuario} !!')