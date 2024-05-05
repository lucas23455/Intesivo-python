class Car():
    def __init__(self,make,model,year):
    #instanciar atributos
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
    #as milhas do carros
        print('Este carro tem ' + str(self.odometer_reading) + ' por milhas !')

#instaciar a classe car
car1 = Car('audi', 'a4', 2016)
print(car1.get_descriptive_name())

# modificando diretamente
car1.odometer_reading = 23
car1.read_odometer()