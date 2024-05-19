import unittest
from teste3 import DadosAnonimos


class Testando_Dados_Anonimos(unittest.TestCase):  

    def setUp(self):
        questao = 'qual linguagem que voce aprendeu?'
        self.meus_dados = DadosAnonimos(questao)
        self.respostas = ['java', 'php', 'ruby']

    def test_store_unico_resposta(self):
        self.meus_dados.store_resposta(self.respostas[0])
        self.assertIn(self.respostas[0], self.meus_dados.respostas)

    def test_store_tres_respostas(self):
        for resposta in self.respostas:
            self.meus_dados.store_resposta(resposta)

        for resposta in self.respostas:
            self.assertIn(resposta, self.meus_dados.respostas)


if __name__ == '__main__':
    unittest.main()
