file_name = 'learning_python.txt'

with open(file_name) as file_object:
	contents = file_object.read()

print(contents)


with open(file_name) as file_object:
	for line in file_object:
		print(line.strip())


with open(file_name) as file_object:
	file_lines = ''
	for line in file_object:
		file_lines += line.lstrip()

if 'def' in file_lines:
	print("\nThis worked")
else:
	print("\nThis did not work")

with open(file_name) as file_object:
	lines = file_object.readlines()
	file_line = ''
	for line in lines:
		file_line += line
		file_line = line.replace('Python', 'C')
		print(file_line.strip())
