class User():
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def perfil_usuario(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O sobrenome da pessoa é {self.sobrenome}')



    def saudaçao(self):
        print(f'ola {self.nome} {self.sobrenome} tudo bem com vc?')



pessoa1 = User('Lucas', 'passos')
pessoa2 = User('maria','souza')
pessoa3 = User('pedro','golvaves')

pessoa1.perfil_usuario()
pessoa1.saudaçao()
print('='*40)
pessoa2.perfil_usuario()
pessoa2.saudaçao()
print('='*40)
pessoa3.perfil_usuario()
pessoa3.saudaçao()