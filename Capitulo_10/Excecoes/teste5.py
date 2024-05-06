
def conta_palavras(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo:
            conteudo = arquivo.read()

    except FileNotFoundError:
        print(f'arquivo {nome_arquivo} não encontrado!!')


    else:
        palavras = conteudo.split()
        num_palavras = len(palavras)

        print(f'O arquivo tem cerca de aproximadamente de {num_palavras} palavras')


nomes_arquivo = ['aladin.tx','alice.txt','moby.txt']

for nome_arquivo in nomes_arquivo:
    conta_palavras(nome_arquivo)