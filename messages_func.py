def send_messages(copy_unsent_messages, sent_messages):
	print("here are the list of messages that were sent")
	while copy_unsent_messages:
		message = copy_unsent_messages.pop()
		print(message)
		sent_messages.append(message)