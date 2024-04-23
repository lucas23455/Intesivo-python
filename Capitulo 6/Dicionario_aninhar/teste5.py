usuario = {

    'aeinstein':{
        'primeiro_nome':'albert',
        'sobrenome': 'einstein',
        'local': 'princeton',
    },

    'mcurie':{
        'primeiro_nome':'marie',
        'sobrenome':'curie',
        'local':'paris',
    },

}

for usuario_nome , usuario_info in usuario.items():
    print(f'\nusuario: {usuario_nome}')
    full_name = usuario_info['primeiro_nome'] + ' ' + usuario_info['sobrenome']
    local = usuario_info['local']

    print('\t full name:'+ full_name.title())
    print('\t local:' + local.title())