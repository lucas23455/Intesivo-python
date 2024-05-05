from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Criando um dado de seis lados
dado_seis_lados = Die()

# Lançando o dado de seis lados dez vezes
print("Lançando o dado de seis lados:")
for _ in range(10):
    print(dado_seis_lados.roll_die())

# Criando um dado de dez lados
dado_dez_lados = Die(10)

# Lançando o dado de dez lados dez vezes
print("\nLançando o dado de dez lados:")
for _ in range(10):
    print(dado_dez_lados.roll_die())

# Criando um dado de vinte lados
dado_vinte_lados = Die(20)

# Lançando o dado de vinte lados dez vezes
print("\nLançando o dado de vinte lados:")
for _ in range(10):
    print(dado_vinte_lados.roll_die())
