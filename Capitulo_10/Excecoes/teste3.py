nome_arquivo = 'alicr.txt'

try:
    with open(nome_arquivo) as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError:
    msg = 'O arquivo ' + nome_arquivo + ' não existe!!'
    print(msg)