def make_pizza(tamanho, *ingredientes):
    print('faça uma ' + str(tamanho) +
          ' pizza com as seguintes ingredientes:')

    for ingrediente in ingredientes:
        print('-' + ingrediente)


make_pizza(16,'peperone')
make_pizza(12,'cogumelos','pimentao','queijo')