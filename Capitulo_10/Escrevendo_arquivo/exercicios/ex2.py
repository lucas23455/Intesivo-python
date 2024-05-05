nome_arquivo = 'guest_book.txt'

print("Bem-vindo ao nosso evento!")

while True:
    nome = input("Por favor, digite seu nome (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        print("Encerrando o programa...")
        break

    saudacao = f"Olá, {nome}! Bem-vindo ao evento."
    print(saudacao)

    # Registra a visita do usuário no arquivo guest_book.txt
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(saudacao + '\n')

print("Obrigado por participar. As visitas foram registradas no arquivo guest_book.txt.")
