def make_sandwiches(*items):
	print("\nItems that will be added to your sandwich")
	for item in items:
		print(item)

make_sandwiches('tomatoes','onions','mayo')
make_sandwiches('onions','mustard','pickels')
make_sandwiches('lettues','tomatoes','pickels','mayo')