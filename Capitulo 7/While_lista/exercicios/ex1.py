sanduiches_pedidos = ['xsalada', 'xegg','baronne', 'costela','xtudo']

sanduiches_preparados = []


while sanduiches_pedidos:
    sanduiches = sanduiches_pedidos.pop()
    print(f'Preparando o seu {sanduiches}')

    print(f'Sanduiche de {sanduiches} pronto! \n')


    sanduiches_preparados.append(sanduiches)


for sanduiche in sanduiches_preparados:
    print(sanduiche)
    