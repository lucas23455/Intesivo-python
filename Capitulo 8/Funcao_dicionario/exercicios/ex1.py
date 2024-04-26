def make_album(nome_artista,titulo_artista,ano_lançamento= ''):
    if ano_lançamento:
        album_musical = {'nome':nome_artista,
                     'titulo':titulo_artista,
                     'ano':ano_lançamento,}
    else:
        album_musical = {'nome': nome_artista,
                         'titulo': titulo_artista,
                         }
    return album_musical


resultados = make_album('roberto carlos','meu amor querido',1985)
print(resultados)

resultados = make_album('coldplay','A head full of dreams',2005)
print(resultados)

resultados = make_album('beyonce','lemode')
print(resultados)