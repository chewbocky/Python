person_0 = {'first_name': 'Manny', 'last_name': 'Terrazas', 'age': 38, 'city': 'Huffman'}

f_name = person_0['first_name'].title()
l_name = person_0['last_name'].title()
age_0 = person_0['age']
city_0 = person_0['city'].title()

print(f"First Name: {f_name}")
print(f"Last Name: {l_name}")
print(f"Age: {age_0}")
print(f"City: {city_0}")



def build_person(first_name, last_name, age=None):
	"""Return a dictionary af infoation about a person"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi','hendrix',age=27)
print(musician)


