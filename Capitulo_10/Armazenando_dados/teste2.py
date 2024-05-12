import json

nome_arquvo = 'numeros.json'

with open(nome_arquvo) as arquivo:
    numeros = json.load(arquivo)

print(numeros)
