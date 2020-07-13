import json

def get_new_number():

	favorite_number = input("What is your favorite number? ")
	filename = 'favorite_number.json'
	with open (filename, 'w') as f:
		json.dump(favorite_number,f)


def get_number():

	filename = 'favorite_number.json'

	try:
		with open (filename) as f:
			number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return number


number = get_number()
if number:
	print(f"I know your favorite number, It is {number}")
else:
	number = get_new_number()
	print(f"We'll remember your favortie number when you come back!")