cidades ={
    'sao paulo':{
        'pais':'brasil',
        'habitantes': 24000
    },
    'bahia':{
        'pais':'brasil',
        'habitantes': 54355
    },
    'pernambuco':{
        'pais':'brasil',
        'habitantes': 65345
    },

}

for chave,valor in cidades.items():
    print(f'\nCidade: {chave}')
    print(f'pais: {valor['pais']}')
    print(f'habitanes: {valor['habitantes']}')