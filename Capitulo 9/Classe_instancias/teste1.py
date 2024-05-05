class Car():
    def __init__(self,make,model,year):
    #instanciar atributos
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


#instaciar a classe car
car1 = Car('audi', 'a4', 2016)
print(car1.get_descriptive_name())

