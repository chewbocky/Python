from random import choice

lotto_numbers = ['1', '23', '20', '15']
lotto_letters = ['r', 'd', 'w', 'g']
win_ticket = []
my_ticket = ['1', 'r', '23', 'w', '15', 'g', '20', 'd']
num_lett = 1
lotto_tries = 1

my_ticket.sort()

while win_ticket != my_ticket:
	win_ticket = []
	if num_lett <= 4:
		win_number = choice(lotto_numbers)
		win_ticket.append(win_number)
		win_letter = choice(lotto_letters)
		win_ticket.append(win_letter)
		num_lett += 1
		print(num_lett)

	lotto_tries += 1
	win_ticket.sort()
	#print(lotto_tries)

print(f"You have finally won the lotto it took you {lotto_tries} tries!")





#print("Who ever has these winning numbers and letters on their ticket wins a prize!")
#print(win_ticket)
