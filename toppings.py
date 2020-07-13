requested_toppings = ['mushrooms','green preppers','extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza!\n")


for topping in requested_toppings:
	print(f"Adding {topping}!")

print("\nFinished making your pizza!\n")

for topping in requested_toppings:
	if topping == 'green preppers':
		print(f"Sorry but we are out of {topping}")
	else:
		print(f"Adding {topping}!")

print("\nFinished making your pizza!\n")



requested_toppings = []

if requested_toppings:
	for topping in requested_toppings:
		print(f"Adding {topping}")
	print("\nFinished making your pizza")
else:
		print("Are you sure you want a plain pizza?\n")




avilable_toppings = ['mushrooms','olives','green preppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in avilable_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"We dont have {requested_topping}")
print("\nFinished making your pizza!")