from classe1 import DadosAnonimos

questao = 'Qual foi sua primeira linguagem de programação?'


meus_dados = DadosAnonimos(questao)


meus_dados.mostrar_questao()
print('Aperte "q" para sair: \n')


while True:
    resposta = input('Linguagem: ')
    if resposta.lower() == 'q':
        break
    meus_dados.store_resposta(resposta)


print('\nObrigado por participar!')
meus_dados.mostra_resultados()
