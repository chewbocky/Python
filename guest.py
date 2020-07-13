filename = 'guest.txt'

with open(filename, 'w') as file_object:
	guest = input("Please type in your name: ")
	file_object.write(guest)