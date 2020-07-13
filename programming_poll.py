filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
	polling = True
	file_object.write("Here are the poll takers and their response.\n")

	while polling:
		print("\nPlease enter 'done' when the polling is finished\n")
		user_poll = input("Please enter your name: ")
		poll = input("Pease explain why you love programming: ")

		if user_poll == 'done':
			break
		elif poll == 'done':
			break
		else:
			file_object.write(f"{user_poll}: {poll}\n")
