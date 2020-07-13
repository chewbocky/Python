'''name = input("Please enter your name: ")


prompt = "If you tell us who you are, we can personalize the massages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name}!")'''

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("(Enter 'q' at anytime to quite)")

	f_name = input("First Name: ")
	if f_name == 'q':
		break
	l_name = input("Last Name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}")