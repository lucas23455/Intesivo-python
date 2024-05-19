import unittest
from classe2 import DadosAnonimos
class TestandoDadosAnonimos(unittest.TestCase):
    def test_store_unico_resposta(self):
        questao = 'Qual foi sua primeira linguagem de programação?'
        meus_dados = DadosAnonimos(questao)
        meus_dados.store_resposta('python')

        self.assertIn('python', meus_dados.respostas)  # verificando se 'python' esta na lista resposta


    def test_store_tres_respostas(self):
        questao = 'qual linguagem que voce aprendeu?'
        meus_dados = DadosAnonimos(questao)
        respostas = ['java','php','ruby']

        for resposta in respostas:
            meus_dados.store_resposta(resposta)


        for resposta in respostas:
            self.assertIn(resposta,meus_dados.respostas)


if __name__ == '__main__':
    unittest.main()
