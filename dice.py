from random import randint

class Dice:

	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		rolls = 1
		while rolls <= self.sides:
			roll = randint(1, self.sides)
			print(roll)
			rolls += 1

		

print("Six Die")
my_die = Dice()
my_die.roll_die()

print("\n10 Die")
my_die = Dice(10)
my_die.roll_die()

print("\n12 Die")
my_die = Dice(12)
my_die.roll_die()
