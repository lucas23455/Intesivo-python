class User:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def perfil_usuario(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O sobrenome da pessoa é {self.sobrenome}')

    def saudacao(self):
        print(f'Olá {self.nome} {self.sobrenome}! Tudo bem com você?')

class Privilegios():
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostre_privilegios(self):
        print('Privilégios:')
        for privilegio in self.privilegios:
            print(privilegio)

class Admin(User):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.privilegios = Privilegios(['adicionar post', 'deletar post', 'banir post'])

    def mostre_privilegios(self):
        self.privilegios.mostre_privilegios()