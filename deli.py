sandwich_orders = ['ham','turkey','roast beef','chicken']
finished_sandwichs = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I made your {current_sandwich} sandwich.")
	finished_sandwichs.append(current_sandwich)

print(finished_sandwichs)


sandwich_orders = ['ham','pastrami','turkey','roast beef','pastrami','chicken']
finished_sandwichs = []

while sandwich_orders:
	while 'pastrami' in sandwich_orders:
		print("The deli has ran out of pastrami")
		sandwich_orders.remove('pastrami')
	current_sandwich = sandwich_orders.pop()
	finished_sandwichs.append(current_sandwich)
	print(f"I have made your {current_sandwich}.")

print(finished_sandwichs)