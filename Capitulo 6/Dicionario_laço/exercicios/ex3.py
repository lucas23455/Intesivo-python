linguagens_favoritas = {
    'jen': 'python',
    'lucas': 'java',
    'pedro': 'php',
    'julia': 'ruby',
    'caio': 'java',
}

pessoas = ['fabio', 'marcos', 'joao']

for pessoa in pessoas:
    if pessoa not in linguagens_favoritas:
        print(f'{pessoa}, por favor, responda à enquete!')

for nome, linguagem in linguagens_favoritas.items():
    print(f'Olá {nome}, sua linguagem favorita é {linguagem}')
