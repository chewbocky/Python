import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
	'''Test if the formatted city function works'''

	def test_first_last_name(self):
		'''Do name like Houston, Texas work?'''
		formatted_city = get_formatted_city('houston','texas')
		self.assertEqual(formatted_city, 'Houston, Texas')

	def test_first_last_name_population(self):
		'''Do name like Houston, Texas  work?'''
		formatted_city = get_formatted_city('houston', 'texas', '1200000000')
		self.assertEqual(formatted_city, 'Houston, Texas, Population: 1200000000')

if __name__ == '__main__':
	unittest.main()