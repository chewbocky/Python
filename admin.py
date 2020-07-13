users = ['mike','garrett','rick','kevin','admin']

for user in users:
	if user == 'admin':
		print(f"\nHello {user.title()}, \nwould you like to see a status reoprt?")
	else:
		print(f"\nHello {user.title()}, thank you for logging in again")


users = []

if users:
	for user in users:
		if user == 'admin':
			print(f"\nHello {user.title()}, \nwould you like to see a status reoprt?")
		else:
			print(f"\nHello {user.title()}, thank you for logging in again")
else:
	print("There are no users")


current_users = ['chewbocky','Gbock','garrettb','bluesmoke','x-wing']
new_users = ['bockg','bockgarrett','statefarm','gbock','linux','cd-rom']

for i in range(len(current_users)):
	current_users[i] = current_users[i].lower()

for n_user in new_users:
	if n_user not in current_users:
		print(f"The user name {n_user} is available.")
	else:
		print(f"You can not use {n_user} as it is already taken.")

c_users = ['gbock','garrettbock','bockgarrett']

for i in range(len(c_users)):
	c_users[i] = c_users[i].upper()

print(c_users)