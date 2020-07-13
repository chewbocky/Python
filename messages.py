'''def show_messages(messages):
	print("Here are the list of messages.")
	for message in messages:
		print(message)

messages = ['Hello User','I like Pizza','I like Beer']

show_messages(messages)
'''

import messages_func
unsent_messages = ['Hello User','I like Pizza','I like Beer']
sent_messages = []

copy_unsent_messages = unsent_messages[:]

messages_func.send_messages(copy_unsent_messages, sent_messages)
print(sent_messages)
print(unsent_messages)


from messages_func import send_messages
unsent_messages = ['Hello User','I like Pizza','I like Beer']
sent_messages = []

copy_unsent_messages = unsent_messages[:]

send_messages(copy_unsent_messages, sent_messages)
print(sent_messages)
print(unsent_messages)


from messages_func import send_messages as sm
unsent_messages = ['Hello User','I like Pizza','I like Beer']
sent_messages = []

copy_unsent_messages = unsent_messages[:]

sm(copy_unsent_messages, sent_messages)
print(sent_messages)
print(unsent_messages)


import messages_func as mf
unsent_messages = ['Hello User','I like Pizza','I like Beer']
sent_messages = []

copy_unsent_messages = unsent_messages[:]

mf.send_messages(copy_unsent_messages, sent_messages)
print(sent_messages)
print(unsent_messages)


from messages_func import *
unsent_messages = ['Hello User','I like Pizza','I like Beer']
sent_messages = []

copy_unsent_messages = unsent_messages[:]

send_messages(copy_unsent_messages, sent_messages)
print(sent_messages)
print(unsent_messages)