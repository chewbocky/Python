filename = 'mound_builders.txt'

with open(filename) as f:
	contents = f.read()
	word = contents.split()
	number = word.count('the')

print(number)