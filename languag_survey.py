from survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What languge did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store the response to the question.
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
	response = input("Languge: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#Show the surevy results.
print("\nThank you to everyone who participated in the surevy!")
my_survey.show_resilts()