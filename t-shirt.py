def make_shirt(message, size='large'):
	print(f"The T-shirt size is {size.upper()}, and the message to be printed is '{message}'")

#make_shirt('large','You read my shirt.')
make_shirt(message='You read my shirt.',size='large')
make_shirt('I love Python.')
make_shirt('I love Python','medium')
make_shirt(size='small',message='This is the 4th time.')