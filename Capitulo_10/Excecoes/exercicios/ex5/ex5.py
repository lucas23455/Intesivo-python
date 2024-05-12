def contar_palavra_em_arquivo(nome_arquivo, palavra):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            # Convertendo o conteúdo para letras minúsculas para contar 'the' independentemente da capitalização
            conteudo_minusculo = conteudo.lower()
            # Contando quantas vezes a palavra 'the' aparece no texto
            ocorrencias = conteudo_minusculo.count(palavra.lower())
            print(f"No arquivo '{nome_arquivo}', a palavra '{palavra}' aparece {ocorrencias} vezes.")
    except FileNotFoundError:
        print(f"Desculpe, o arquivo '{nome_arquivo}' não foi encontrado.")

# Chamando a função para contar a palavra 'the' em cada arquivo
contar_palavra_em_arquivo('livro.txt', 'the')
contar_palavra_em_arquivo('texto2.txt', 'the')
# Adicione mais chamadas à função para outros arquivos, se necessário
