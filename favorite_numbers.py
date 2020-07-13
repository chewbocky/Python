favorite_numbers = {'Manny': [2, 69], 'Daniel': [4, 777], 'Jared': [7, 747], 'John': [10, 100], 'Davitt': [12, 300]}

print(f"Manny's favorite number is {favorite_numbers['Manny']}")
print(f"Daniel's favorite number is {favorite_numbers['Daniel']}")
print(f"Jared's favorite number is {favorite_numbers['Jared']}")
print(f"John's favorite number is {favorite_numbers['John']}")
print(f"Davitt's favorite number is {favorite_numbers['Davitt']}")


for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")