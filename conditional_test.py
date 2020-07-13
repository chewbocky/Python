car = 'subaru'
print("Is car == 'subaru'? I predict true")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false")
print(car == 'audi')


lunch = 'PIZzA'
print("\nIs 'pizza' on the lunch menu?")
print(lunch.lower() == 'pizza')



numbers = [20,45,23,78,90]
fixed_num = 25
num_0 = 5
num_1 = 25
for number in numbers:
	if number >= fixed_num:
		print(f"{number} is greater then {fixed_num}!")
	else:
		print(f"{number} is less then {fixed_num}")


for number in numbers:
	if number >= num_0 and number <= num_1:
		print(f"{number} is between {num_0} and {num_1}.")
	else:
		print(f"{number} in not between {num_0} and {num_1}.")


menu_items = ['pizza','fish','soup','pasta','salad']

for item in menu_items:
	if item == 'pizza':
		print("Pizza is on the Menu today!")
	else:
		print(f"{item} is also on the menu today.")