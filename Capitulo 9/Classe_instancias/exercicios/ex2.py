class User:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.login_attempts = 0

    def perfil_usuario(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O sobrenome da pessoa é {self.sobrenome}')

    def saudacao(self):
        print(f'Olá {self.nome} {self.sobrenome}, tudo bem com você?')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Creating an instance of the User class
usuario = User('Lucas', 'Passos')

# Incrementing login attempts several times
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()

# Displaying the value of login attempts
print("Login attempts:", usuario.login_attempts)

# Resetting login attempts
usuario.reset_login_attempts()

# Displaying login attempts again to ensure it's reset
print("Login attempts after reset:", usuario.login_attempts)
