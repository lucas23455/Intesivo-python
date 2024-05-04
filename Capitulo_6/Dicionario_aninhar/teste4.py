linguagem_favorita = {
    'lucas': ['python','ruby'],
    'julia': ['java','java script'],
    'pedro': ['php','rust'],
}

for name, linguagem in linguagem_favorita.items():
    print(f'\n{name.title()} e sua linguagens favoritas sao:')

    for l in linguagem:
        print(l)
