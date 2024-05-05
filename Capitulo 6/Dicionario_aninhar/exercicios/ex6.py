# Dicionário representando um animal de estimação
animal1 = {'nome': 'Buddy',
           'tipo': 'Cachorro',
           'idade': 3,
           'dono': 'Alice',
           'vacinas': ['Raiva', 'Moquillo']}

# Dicionário representando outro animal de estimação
animal2 = {'nome': 'Whiskers',
           'tipo': 'Gato',
           'idade': 2,
           'dono': 'Bob',
           'vacinas': ['Leucemia Felina', 'Rinotraqueíte']}

# Dicionário representando outro animal de estimação
animal3 = {'nome': 'Nibbles',
           'tipo': 'Coelho',
           'idade': 1,
           'dono': 'Charlie',
           'vacinas': ['Mixomatose', 'Calicivirose']}

# Lista para armazenar todos os animais de estimação
animais = [animal1, animal2, animal3]

# Percorra a lista de animais de estimação e exiba suas informações
for animal in animais:
    print("Nome do Animal:", animal['nome'])
    print("Tipo:", animal['tipo'])
    print("Idade:", animal['idade'])
    print("Dono:", animal['dono'])
    print("Vacinas:", ', '.join(animal['vacinas']))  # Juntando a lista de vacinas com vírgulas

