def make_pizza(tamanho,*ingredientes):
    print(f'\nfazer uma {tamanho} inch pizza com os seguintes ingredientes:')

    for ingrediente in ingredientes:
        print(f'- {ingrediente}')