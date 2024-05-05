nomes = ['carlos','micael','enzo','henrique','jose','gabriel']

novos_usuarios = ['maria','juliana','henrique','esther','maria','GABRIEL']


for novo_usuario in novos_usuarios:
    if novo_usuario.lower() in nomes:
        print('Esse nome: '+ novo_usuario +' ja esta na lista')
    else:
        print(novo_usuario)