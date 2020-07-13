class Users:

	def __init__(self, first_name, last_name, username, dept):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.dept = dept
		self.login_attempts = 0

	def describe_user(self):
		print(f"First Name: {self.first_name.title()}")
		print(f"Last Name: {self.last_name.title()}")
		print(f"Username: {self.username}")
		print(f"Department: {self.dept}")

	def greet_user(self):
		print(f"\nHello and Welcome, {self.first_name.title()} {self.last_name.title()}")

	def increment_login_attempts(self,logins):
		self.login_attempts += logins
		print(f"Number of login attempts: {self.login_attempts}")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(self.login_attempts)