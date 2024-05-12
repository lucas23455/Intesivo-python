import json

def salvar_numero_favorito():
    numero_favorito = input("Qual é o seu número favorito? ")
    with open('numero_favorito.json', 'w') as arquivo:
        json.dump(numero_favorito, arquivo)
    print("Número favorito salvo com sucesso!")

def carregar_numero_favorito():
    try:
        with open('numero_favorito.json', 'r') as arquivo:
            numero_favorito = json.load(arquivo)
            print(f"Eu sei qual é o seu número favorito! É {numero_favorito}.")
    except FileNotFoundError:
        print("Você ainda não salvou um número favorito.")

# Salvar o número favorito
salvar_numero_favorito()

# Carregar e exibir o número favorito
carregar_numero_favorito()
