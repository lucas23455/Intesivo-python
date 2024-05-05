class Carro():
    def __init__(self,feito,modelo,ano):
        self.feito = feito
        self.modelo = modelo
        self.ano = ano
        self.quilometros_rodados = 0


    def descrever_nome(self):
        nome_full = str(self.ano) + ' ' + self.modelo + ' ' + self.feito
        return nome_full.title()


    def ler_quilometros(self):
        print(f'Este carro tem {self.quilometros_rodados} por milhas !!')



    def quilometro_atualizado(self,quilometragem):
        if quilometragem >= self.quilometros_rodados:
            self.quilometros_rodados = quilometragem
        else:
            print('voce não pode voltar a quilometragem!!')


    def incrementar_quilometro(self,milhas):
        self.quilometros_rodados += milhas

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


#classe filha
class Carro_eletrico(Carro):
    def __init__(self,feito,modelo,ano):
        """inicializado os atributos da classe pai"""
        super().__init__(feito,modelo,ano)
        """ pegando caracteristas da classe bateria """
        self.bateria = Bateria()

    #subsescrevendo
    def taque_gasolina():
        print('esta carro não precisa de um taque de gas')


meu_tesla = Carro_eletrico('tesla','models','2020')
print(meu_tesla.descrever_nome())
meu_tesla.bateria.descrever_bateria()
meu_tesla.bateria.get_range()

