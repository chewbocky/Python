class Employee:

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, salary, add_salary = 5000):
		self.salary += add_salary
		return self.salary
		print(f"The employee's new salary is: {self.salary}")

