vacations = {}

active = True

while active:
	name = input("What is your name? ")
	place = input("What is the one place that you would like to go? ")
	add = input("Is there anyone else that wants to add to the list? (yes/no)")

	vacations[name] = place

	if add == 'no':
		active = False

print("\n --- Poll Results ---")
for name, place in vacations.items():
	print(f"{name.title()} would like to go to {place.title()}.")

