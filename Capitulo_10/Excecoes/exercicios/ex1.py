try:
    num1 = int(input('digite o primeiro numero:'))
    num2 = int(input('digite o segundo numero:'))
    soma = num1+num2

    print(f'o valor sera {soma}')

except ValueError:
    print('não pode colocar letra na entrada')



