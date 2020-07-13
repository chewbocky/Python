favorite_places = {
	'mark': ['church','frys','nature'],
	'jeremy': ['home', 'brewery','nature'],
	'stacey': ['nature','park','home']
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")