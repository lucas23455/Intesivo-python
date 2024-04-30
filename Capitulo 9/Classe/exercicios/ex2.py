class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is open!")


# Instância 1
restaurante1 = Restaurant("Sabor do Brasil", "Brasileira")
restaurante1.describe_restaurant()

# Instância 2
restaurante2 = Restaurant("Sushi Delight", "Japanese")
restaurante2.describe_restaurant()

# Instância 3
restaurante3 = Restaurant("Pizza Place", "Italian")
restaurante3.describe_restaurant()
