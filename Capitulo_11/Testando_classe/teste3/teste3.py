class DadosAnonimos:
    def __init__(self, questao):
        self.questao = questao
        self.respostas = []

    def mostrar_questao(self):
        print(self.questao)

    def store_resposta(self, nova_resposta):
        self.respostas.append(nova_resposta)

    def mostra_resultados(self):
        print('RESULTADOS:')
        for resposta in self.respostas:
            print('- ' + resposta)


