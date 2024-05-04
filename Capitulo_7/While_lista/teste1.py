usuario_Nconfirmados = ['Alice', 'Marcos','João']

usuario_confirmados = []

# vai remover o ultimo nome da lista de usuario não confirmado
# e vai colocar na lista usuario confirmado
while usuario_Nconfirmados:
    usuario = usuario_Nconfirmados.pop()

    print(f'Verificando usuario: {usuario.title()}')

    usuario_confirmados.append(usuario)

print('\nOs usuario já foram confirmados:')
for usuario_confirmado in usuario_confirmados:
        print(usuario_confirmado.title())