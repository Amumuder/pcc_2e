class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name}: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is open.')

    def set_number_served(self, customers):
        self.number_served = customers
        print(f'Customers Served: {self.number_served}')

    def increment_number_served(self, increment_customers):
        self.number_served += increment_customers
        print(f'Customers Served: {self.number_served}')
