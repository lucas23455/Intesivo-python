class User:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def perfil_usuario(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O sobrenome da pessoa é {self.sobrenome}')

    def saudacao(self):
        print(f'Olá {self.nome} {self.sobrenome}! Tudo bem com você?')