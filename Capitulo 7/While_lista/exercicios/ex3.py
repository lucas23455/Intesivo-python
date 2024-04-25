# Lista para armazenar as respostas dos usuários
respostas = []

# Realizar a enquete
print("Enquete: Férias dos Sonhos")
print("Responda à pergunta abaixo (ou digite 'sair' para encerrar a enquete).")
while True:
    resposta = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    if resposta.lower() == 'sair':
        break
    else:
        respostas.append(resposta)

# Apresentar os resultados da enquete
print("\nResultados da Enquete:")
print("----------------------------")
if respostas:
    print("As férias dos sonhos dos usuários são:")
    for resposta in respostas:
        print(resposta)
else:
    print("Nenhuma resposta foi registrada.")
