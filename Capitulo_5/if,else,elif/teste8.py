ingredientes_disponiveis = ['cogumelos','azeite','pimentao','peperone','abacaxi',
                            'cheese extra']

ingredientes_pedidos = ['cogumelos','batata frita','cheese extra']

for ingrediente_pedido in ingredientes_pedidos:
    if ingrediente_pedido in ingredientes_disponiveis:
        print('adione ' + ingrediente_pedido + '.')

    else:
        print('desculpe , nós não temos : ' + ingrediente_pedido + '.')

print('Esta pronta a sua pizza!!')

