my_pizza = ['cheese','pepperoni','bacon','sausage','surpreme']
friend_pizza = my_pizza[:]

my_pizza.append('bbq')
friend_pizza.append('chicken')

print(my_pizza)
print(friend_pizza)

for pizza in my_pizza:
	print(pizza)

for pizza in friend_pizza:
	print(pizza)



#store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")




toppings = []
prompt = "\nPlease enter the type of topping you want on your pizza."
prompt += "\n(Enter 'quit' when you have entered all of your toppings."
prompt += "\nTopping: "
active = True

while active:
	message = input(prompt)
	if message != 'quit':
		toppings.append(message)
	else:
		active = False

print("\nHere are the toppings that will be added to your pizza:")
for topping in toppings:
	print(topping.title())
