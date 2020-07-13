import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		'''Create a survey and test a set of responses for use in all test methods.'''
		first = 'Garrett'
		last = 'Bock'
		salary = 80000 
		self.default_salary = 85000
		self.my_employee = Employee(first, last, salary)

	def test_default_salary(self):
		self.my_employee.give_raise(self)
		self.assertEqual(self.default_salary, self.my_employee.salary)

if __name__ == '__main__':
	unittest.main()