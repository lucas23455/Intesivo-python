unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    #retirando os elementos da lista
    current_design = unprinted_designs.pop()

    print('Imprimindo modelo:'+ current_design)

    #colocando em outra lista
    completed_models.append(current_design)


print('\nOs modelos imprimidos:')

for completed_model in completed_models:
    print(completed_model)
