nome_arquivo = 'alice.txt'

try:
    with open(nome_arquivo) as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError:
    msg = 'O arquivo ' + nome_arquivo + ' não existe!!'
    print(msg)

else:
    palavras = conteudo.split() #coloca em uma lista
    num_palavras = len(palavras) #conta todas as palavras
    print(f'O arquivo {nome_arquivo} tem cerca de aproximadamente {str(num_palavras)} palavras!!')
