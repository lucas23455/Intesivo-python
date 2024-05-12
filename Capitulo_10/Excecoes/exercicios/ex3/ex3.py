def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
    except FileNotFoundError:
        print(f"Desculpe, o arquivo '{nome_arquivo}' não foi encontrado.")

# Tentar ler o arquivo cats.txt
ler_arquivo('caess.txt')

# Tentar ler o arquivo dogs.txt
ler_arquivo('gatos.txt')
