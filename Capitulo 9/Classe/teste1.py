class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + ' senta agora!!')

    def rolar(self):
        print(self.nome.title() + ' agora role!!')

# Fora da classe Cachorro
meu_cao = Cachorro('Rex', 9)
seu_cao = Cachorro('pedro',5)
nosso_cao = Cachorro('saul',4)

print('O nome do meu cão é ' + meu_cao.nome.title() + '.')
print('O meu cao tem '+ str(meu_cao.idade) + ' anos de idade!!')
meu_cao.sentar()

print('='*20)

print('O nome do meu cão é ' + seu_cao.nome.title() + '.')
print('O meu cao tem '+ str(seu_cao.idade) + ' anos de idade!!')
seu_cao.rolar()

print('='*20)

print('O nome do meu cão é ' + nosso_cao.nome.title() + '.')
print('O meu cao tem '+ str(nosso_cao.idade) + ' anos de idade!!')
nosso_cao.rolar()