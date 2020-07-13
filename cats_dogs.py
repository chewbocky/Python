def file_read(file):
	try:
		with open(file) as f:
			contents = f.read()
	except FileNotFoundError:
		#print(f"\nThe file {file} was not found.")
		pass
	else:
		print(f"\nHere are the contents for file {file}")
		print(contents)

files = ['dogs.txt','cats.txt']
for file in files:
	file_read(file)


