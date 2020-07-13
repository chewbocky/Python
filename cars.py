cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


cars = ['bmw','audi','toyota','subaru']
print("Here is the orginal list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the orginal list again:")
print(cars)


cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)



#IF Statements
cars = ['bmw','audi','toyota','subaru']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


car = 'subaru'
print("\nIs car == 'subaru'? I predict true")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false")
print(car == 'audi')


def cars(n_make, n_model, **car_info):
	car_info['make'] = n_make
	car_info['model'] = n_model
	return car_info

car = cars('Chevy','Express',color= 'Blue', tow_packtage= True)
print("\n Here is the car info.")
print(car)