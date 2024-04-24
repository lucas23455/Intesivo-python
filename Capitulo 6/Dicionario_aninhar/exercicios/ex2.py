pet1 = {
    'nome': 'lalu',
    'dono': 'lucas',
    'idade': 5,
    'local': 'rua monte belo',
}

pet2 = {
    'nome': 'gol',
    'dono': 'pedro',
    'idade': 3,
    'local': 'rua catole',
}

pet3 = {
    'nome': 'rex',
    'dono': 'maria',
    'idade': 6,
    'local': 'av marechal tito',
}


pets = [pet1,pet2,pet3]


for pet in pets:
    print(f'\nNome do cao: {pet['nome']}')
    print(f'Nome do dono: {pet['dono']}')
    print(f'Idade: {pet['idade']} anos')
    print(f'local: {pet['local']}')





