people = 0
people_count = 1
people_age = []
ticket_cost = 0
baby = 0
child = 10
adult = 12

people_prompt = "How many people will be seeing the movie today? "
people = input(people_prompt)
people = int(people)

while people_count <= people:
	people_prompt = "What is the age of the person: "
	age = input(people_prompt)
	age = int(age)
	people_age.append(age)
	people_count += 1

print("Here are the ages")
for person in people_age:
	print(f"  {person}")

for person in people_age:	
	if person < 3:
		print("Their cost is: $0")
	elif person <= 12:
		print("Their cost is: $10")
		ticket_cost += child
	else:
		print("Their cost is: $12")
		ticket_cost += adult

print(f"The total cost is: {ticket_cost}")

