print('bem vindo ao pizzaria')

ingrediente_pizza = []

active = True
while active:
    ingredientes = input('Que ingrediente deseja colocar na pizza? (digite "quit" para sair) ')

    if ingredientes.lower() == 'quit':
        print('Encerrando o programa...')
        active = False

    ingrediente_pizza.append(ingredientes)
    print(f'Adicionado {ingredientes} à pizza')

print('\nOs seguintes ingredientes foram adicionados à sua pizza:')
for ingrediente in ingrediente_pizza:
    print('- ' + ingrediente)

print('Obrigado por pedir na nossa pizzaria! Sua pizza está a caminho!')
