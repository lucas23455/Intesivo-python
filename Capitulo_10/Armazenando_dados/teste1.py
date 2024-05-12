import json

numeros = [1,4,6,7,8,20,9]

nome_arquivo = 'numeros.json'
with open(nome_arquivo,'w') as arquivo:
    json.dump(numeros,arquivo)
