respones = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and responce.
	name = input("\nWhat is your name? ")
	responce = input("which mountain would you like to climb someday? ")

	# Store the responce in the dictionary
	respones[name] = responce

	# find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# polling is complete. Show the results.
print("\n--- Poll results ---")
for name, responce in respones.items():
	print(f"{name.title()} would like to clime {responce.title()}.")