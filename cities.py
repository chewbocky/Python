cities = {
	'houston': {
		'state': 'texas',
		'contury': 'usa',
		'weather': 'hot'
	},
	'cairo': {
		'state': 'n/a',
		'contury': 'egypt',
		'weather': 'hot'
	},
	'pittsburg': {
		'state': 'pennsylvania',
		'contury': 'usa',
		'weather': 'cold'
	}
}


for city, info in cities.items():
	print(f"\nHere are some facts about {city.title()}")
	print(f"\tit's state is: {info['state'].title()}")
	print(f"\tit's contury is: {info['contury'].title()}")
	print(f"\tit's weather is: {info['weather'].title()}")


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")