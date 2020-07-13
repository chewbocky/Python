from users import Users

class Privileges:
	def __init__(self):
		self.privileges = ['can add a post','can delete a post','can modify a post']

	def show_privileges(self):
		print("\nHere is a list of rights a Admin has:")
		for privilege in self.privileges:
			print(privilege)


class Admin(Users):
	def __init__(self, first_name, last_name, username, dept):
		super().__init__(first_name, last_name, username, dept)
		self.privilege = Privileges()