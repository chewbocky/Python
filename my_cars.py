from car import Car 
from electric_car import ElectricCar

my_beetle = Car('volkswagen','beetle','2019')
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())


from electric_car import ElectricCar as EC 
my_tesla = EC('tesla','model s','2019')
print(my_tesla.get_descriptive_name())