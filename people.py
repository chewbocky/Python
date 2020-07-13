person_0 = {'first_name': 'Manny', 'last_name': 'Terrazas', 'age': 38, 'city': 'Huffman'}
person_1 = {'first_name': 'Fred', 'last_name': 'Bock', 'age': 60, 'city': 'Pasadena'}
person_2 = {'first_name': 'Jeremy', 'last_name': 'Easten-Marks', 'age': 40, 'city': 'Houston'}

people = [person_0, person_1, person_2]

f_name = person_0['first_name'].title()
l_name = person_0['last_name'].title()
age_0 = person_0['age']
city_0 = person_0['city'].title()

print(f"First Name: {f_name}")
print(f"Last Name: {l_name}")
print(f"Age: {age_0}")
print(f"City: {city_0}")




for person in people:
	print(f"\n Full Name: {person['first_name'].title()} {person['last_name']}")
	print(f"\t Age: {person['age']}")
	print(f"\t Location: {person['city']}")