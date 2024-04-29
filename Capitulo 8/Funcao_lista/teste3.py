def print_models (unprinted_designs, completed_models):
    # retirando os elementos da lista
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Imprimindo modelo:' + current_design)

        # colocando em outra lista
        completed_models.append(current_design)



def show_completed_models(completed_models):
    print('\nOs modelos imprimidos:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot penda', 'docecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

print(unprinted_designs)

