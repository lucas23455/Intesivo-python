class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is open!")


# Criando uma instância da classe Restaurant
restaurant = Restaurant("Saboroso", "Brasileira")

# Mostrando os atributos individualmente
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Chamando os métodos
restaurant.describe_restaurant()
restaurant.open_restaurant()
