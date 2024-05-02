from teste1 import Carro

class Bateria():
    def __init__(self,bateria_carga = 70):
        self.bateria_carga = bateria_carga

    def descrever_bateria(self):
        print(f'este carro tem {str(self.bateria_carga)} kwh de bateria')


    def get_range(self):
        if self.bateria_carga == 70:
            range = 240
        elif self.bateria_carga == 85:
            range = 270

        mensagem = 'este carro pode ir aproximadamente ' + str(range)
        mensagem += ' milhas cheia'
        print(mensagem)


class Carro_eletrico(Carro):
    def __init__(self,feito,modelo,ano):
        """inicializado os atributos da classe pai"""
        super().__init__(feito,modelo,ano)
        """ pegando caracteristas da classe bateria """
        self.bateria = Bateria()

    #subsescrevendo
    def taque_gasolina():
        print('esta carro não precisa de um taque de gas')