class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is open!")


#CLASSE FILHA
class Sorveteria(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name,cuisine_type)
        self.sabores = []


    def mostre_sabores(self):
        print('Avaliando os sabores de sorvete!')
        for sabor in self.sabores:
            print('-'+ sabor)



