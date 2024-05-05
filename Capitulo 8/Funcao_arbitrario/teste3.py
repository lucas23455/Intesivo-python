def montando_perfil(primeiro_nome, sobrenome, **info_usuario):
    perfil = {}
    perfil['primeiro_nome'] = primeiro_nome
    perfil['sobrenome'] = sobrenome

    for chave, valor in info_usuario.items():
        perfil[chave] = valor
    return perfil

usuario = montando_perfil('albert',
                          'einsteins',
                          location='princeton',
                          campo='fisica',
                          idade = 45,
                          )

print(usuario)
