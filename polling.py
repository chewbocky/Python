users = ['manny','fred','jeremy','erick','jen','sarah','edward','phil','vicky']

pollers = {
	'manny': 'bat',
	'fred': 'c++',
	'jeremy': 'python',
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python'
}

for user in users:
	if user in pollers.keys():
		print(f"{user.title()}, Thank you for take the time to answer the poll.")
	else:
		print(f"{user.title()}, Please take the time to answer the poll.")