class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type 
		self.number_served = 0

	def describe_restaurant(self):
		print(f"\nThe name of the restaurant is {self.restaurant_name}")
		print(f"The cuisine type is {self.cuisine_type}")

	def open_restaurant(self):
		print("\nThe restaurant is OPEN")

	def set_numbered_served(self):
		print(f"The number of people served is {self.number_served}")

	def increment_number_served(self, served):
		self.number_served += served


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.icecream_flavors = ['chocolate', 'vanilla','cherry','raspberry']

	def get_flavors(self):
		print("\nHere are the available flavors")
		for flavor in self.icecream_flavors:
			print(flavor)