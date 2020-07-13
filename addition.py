print("Please enter two numbers and I will add them togeather")
print("please type 'q' to quit")

while True:
	first_number = input("\nFirst Number: ")

	if first_number == 'q':
		break
	try:
		first_number = int(first_number)
	except ValueError:
		print("Sorry, but you must enter a number.")


	second_number = input("Second Number: ")
	if second_number == 'q':
		break
	try:
		second_number = int(second_number)
	except ValueError:
		print("Sorry, but you must enter a number.")

	try:
		answer = first_number + second_number
	except TypeError:
		pass
	else:
		print(answer)

