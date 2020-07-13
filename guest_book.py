filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
	guest_active = True
	file_object.write("These are the names for the guest that attened the party:\n")
	while True:
		print("\nPlease enter your name for the record")
		print("(If all guests have signed in please type in 'done')")
		guest = input("name: ")
		if guest == 'done':
			break
		else:
			print(f"\nHello, {guest} and welcome to the party!")
			file_object.write(f"{guest}\n")
