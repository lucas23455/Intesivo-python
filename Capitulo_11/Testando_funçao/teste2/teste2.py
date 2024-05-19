def usuario(nome,sobrenome, meio= ''):
    if meio:
        full_nome = nome + ' ' + sobrenome + ' ' + meio
    else:
        full_nome = nome + ' ' + sobrenome
    return full_nome.title()


