rivers = {'nile': "egypt",
		  'mississippi': 'usa',
		  'amazon': 'brazil'}

for river, contury in rivers.items():
	if contury == 'usa':
		print(f"The {river.title()} runs though {contury.upper()}.")
	else:
		print(f"The {river.title()} runs though {contury.title()}.")

for river in rivers.keys():
	print(river)

for contury in rivers.values():
	print(contury)