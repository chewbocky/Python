alien_color = 'yellow'

if alien_color.lower() == 'green':
	print("You shot down a Green alien and you have earned 5 points.")
elif alien_color.lower() == 'red':
	print("You shot down a Red alien and you have earned 10 points.")
else:
	print("You shot down a Yellow alien and you have earned 15 points.")

alien_color = 'green'

if alien_color.lower() == 'green':
	print("You shot down a Green alien and you have earned 5 points.")
elif alien_color.lower() != 'green':
	print("You shot down a non Green alien and you have earned 10 points.")
