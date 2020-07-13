file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()

	birthday = input("Enter your birthday, in the formay MMDDYY: ")
	if birthday in pi_string:
		print("Your birthday appers in the first million digits of PI!")
	else:
		print("Your birthday does not show up in the first million digits of PI.")

	print(f"{pi_string[:52]}...")
	print(len(pi_string)) 