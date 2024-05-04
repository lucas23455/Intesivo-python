linguagens_favoritas = {
    'jen': 'python',
    'lucas': 'java',
    'pedro': 'php',
    'julia': 'ruby',
    'caio': 'java',
}


amigos = ['lucas','pedro']

for nome in linguagens_favoritas.keys():
    print(nome.title())

    if nome in amigos:
        print(f'Oi {nome.title()} sua linguagem favorite é : {linguagens_favoritas[nome]}')