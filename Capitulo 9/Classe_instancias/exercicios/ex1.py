class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is open!")

    def set_number_served(self,number):
        self.number_served = number


    def increment_number_served(self,increment):
        self.number_served += increment



restaurant = Restaurant("Saboroso", "Brasileira")

# Displaying the initial number of customers served
print("Number of customers served initially:", restaurant.number_served)

# Modifying the number of customers served
restaurant.number_served = 50
print("Number of customers served after modification:", restaurant.number_served)

# Using the set_number_served method
restaurant.set_number_served(100)
print("Number of customers served after using set_number_served method:", restaurant.number_served)

# Using the increment_number_served method
restaurant.increment_number_served(30)
print("Number of customers served after using increment_number_served method:", restaurant.number_served)