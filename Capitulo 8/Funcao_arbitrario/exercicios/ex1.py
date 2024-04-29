def make_sandwich(*ingredientes):
    print('\ningredientes:')
    for ingrediente in ingredientes:
        print(f'-{ingrediente}')



make_sandwich('tomate','carne','queijo','ketshup','mostarda')
make_sandwich('alface','tomate')
make_sandwich('queijo','picles','feijao')