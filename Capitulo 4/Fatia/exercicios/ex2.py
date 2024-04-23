my_pizzas = ['peperone','calabreza','baiana']
friends_pizzas = my_pizzas[:]

my_pizzas.append('portuguesa')
print(f' minhas pizzas favoritas são: {my_pizzas}')

for pizza in my_pizzas:
    print(pizza)

friends_pizzas.append('romeo e julieta')
print(f'As pizzas favoritas do meu amigo são:{friends_pizzas}')

for pizza in friends_pizzas:
    print(pizza)