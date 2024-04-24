lugares_favoritos = {
    'pessoa1': {'nome': 'Pedro', 'local': 'Paris'},
    'pessoa2': {'nome': 'Marcos', 'local': 'EUA'},
    'pessoa3': {'nome': 'Maria', 'local': 'México'}
}

for pessoa, info in lugares_favoritos.items():
    print(f"\nO lugar favorito de {info['nome']} é {info['local']}.")
