def make_pizza(*ingredientes):
    for ingrediente in ingredientes:
        print('-' + ingrediente)


make_pizza('peperone')
make_pizza('cogumelo','pimentao verde','queijo')