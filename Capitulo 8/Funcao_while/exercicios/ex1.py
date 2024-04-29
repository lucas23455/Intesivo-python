def make_album(nome_artista,titulo_artista,ano_lançamento = ''):
    if ano_lançamento:
        album_musical = {'nome':nome_artista,
                     'titulo':titulo_artista,
                     'ano':ano_lançamento,}
    else:
        album_musical = {'nome': nome_artista,
                         'titulo': titulo_artista,
                         }
    return album_musical


while True:
    n_artista = input('qual o nome do artista ?')
    t_artista = input('qual o titulo da musica?')
    a_artista = input('ano de lançamento?')

    resultado = make_album(n_artista,t_artista,a_artista)
    print(resultado)

    sair = input('deseja continuar ? (s/n)')

    if a_artista == '':
        continue

    if sair == 'n':
        print('encerrando o programa...')
        break