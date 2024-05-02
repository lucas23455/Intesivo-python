class Carro():

    def __init__(self,feito,modelo,ano):
        self.feito = feito
        self.modelo = modelo
        self.ano = ano
        self.velocimentro = 0


    def descrever_carro(self):
        nome_full = str(self.ano)+ ' ' + self.feito + ' ' + self.modelo
        return nome_full.title()

    def ler_velocimetro(self):
        print(f'Este carro tem {str(self.velocimentro)} em milhas!')



    def atualizar_velocimetro(self,quilometragem):

        if quilometragem >= self.ler_velocimentro:
            self.ler_velocimentro = quilometragem

        else:
            print('Voce não pode voltar velocimetro!!')


    def atualizar_velocimetro(self,milhas):
        self.ler_velocimentro += milhas