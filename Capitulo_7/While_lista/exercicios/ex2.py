# Criar lista de pedidos de sanduíches
sandwich_orders = ['sanduíche de atum', 'sanduíche de pastrami', 'sanduíche de frango', 'sanduíche de pastrami', 'sanduíche de vegetariano', 'sanduíche de pastrami', 'sanduíche de presunto e queijo']

# Exibir mensagem informando que a lanchonete está sem pastrami
print("Desculpe, estamos sem pastrami no momento.\n")

# Remover todas as ocorrências de 'pastrami' da lista de pedidos de sanduíches
while 'sanduíche de pastrami' in sandwich_orders:
    sandwich_orders.remove('sanduíche de pastrami')

# Criar lista vazia para os sanduíches preparados
finished_sandwiches = []

# Preparar cada sanduíche pedido
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Preparando o seu {sandwich}...")
    # Simular preparo do sanduíche
    print(f"Sanduíche de {sandwich} pronto!\n")
    # Adicionar sanduíche preparado à lista de sanduíches prontos
    finished_sandwiches.append(sandwich)

# Mostrar mensagem com os sanduíches preparados
print("Os seguintes sanduíches foram preparados:")
for sandwich in finished_sandwiches:
    print(sandwich)
