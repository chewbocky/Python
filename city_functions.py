def get_formatted_city(city, country, population=''):
	'''Put a city name in a nice formatted way'''

	if population:
		formatted_city = f"{city}, {country}, population: {population}"
	else:
		formatted_city = f"{city}, {country}"

	return formatted_city.title()