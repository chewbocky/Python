def describe_pet(pet_name,animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type.title()}.")
	print(f"My {animal_type.title()}'s name is {pet_name.title()}.")




pet_0 = {'name': 'scout', 'animal_kind': 'dog', 'owner': 'Garrett'}
pet_1 = {'name': 'phantom', 'animal_kind': 'dog', 'owner': 'Garrett'}
pet_2 = {'name': 'kirby', 'animal_kind': 'hamester', 'owner': 'Garrett'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(f"\nName: {pet['name'].title()}")
	print(f"\tAnimal Type: {pet['animal_kind'].title()}")
	print(f"\t Owner: {pet['owner'].title()}")


pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)



describe_pet('harry', 'hamester')
describe_pet(animal_type='hamester',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamester')

describe_pet(pet_name='willie')
describe_pet('willie')