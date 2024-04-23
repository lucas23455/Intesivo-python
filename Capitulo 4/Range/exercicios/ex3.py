numeros_pares = []
numeros_impares = []
for value in range(1,21):
    if value %2 == 0:
        numeros_pares.append(value)
    else:
        numeros_impares.append(value)


print(f'os numeros pares sao: {numeros_pares}')
print(f'os numeros impares sao: {numeros_impares}')