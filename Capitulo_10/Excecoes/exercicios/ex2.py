while True:
    try:
        num1 = input('Digite o primeiro número (ou "s" para sair): ')
        if num1.lower() == 's':
            print('Encerrando o programa!')
            break

        num1 = int(num1)

        num2 = input('Digite o segundo número (ou "s" para sair): ')
        if num2.lower() == 's':
            print('Encerrando o programa!')
            break

        num2 = int(num2)

        soma = num1 + num2
        print(f'A soma dos números é: {soma}')

    except ValueError:
        print('Não é possível somar letras! Por favor, insira apenas números ou "s" para sair.')
