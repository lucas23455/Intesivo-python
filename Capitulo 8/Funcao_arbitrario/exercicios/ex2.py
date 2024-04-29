def montando_perfil(primeiro_nome,sobrenome,**info):
    perfil = {}
    perfil['primeiro_nome'] = primeiro_nome
    perfil['sobrenome'] = sobrenome

    for chave , valor in info.items():
        perfil[chave] = valor
    return perfil

usuario = montando_perfil('lucas','passos',local = 'sao paulo', idade = 21 , )

print(usuario)

    