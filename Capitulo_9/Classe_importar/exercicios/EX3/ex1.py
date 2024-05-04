from user import User
from admini import Admin


pessoa1 = User('Lucas','passos')
pessoa2 = User('Maria', 'Souza')
pessoa3 = User('Pedro', 'Goulart')

pessoa1.perfil_usuario()
pessoa1.saudacao()
print('=' * 40)
pessoa2.perfil_usuario()
pessoa2.saudacao()
print('=' * 40)
pessoa3.perfil_usuario()
pessoa3.saudacao()
print('=' * 40)

admin = Admin('Admin', 'User')
admin.perfil_usuario()
admin.saudacao()
admin.mostre_privilegios()
