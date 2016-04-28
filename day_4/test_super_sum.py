'''
Test suite for super_sum
'''
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
	"""Test Case for super_sum """
	def test_empty_input(self):
		''' tests empty input'''

		self.assertEqual(super_sum(), 0)

	def test_sum_of_integers(self):
		"""
		Tests sum of integers
		"""

		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertNotEqual(super_sum(10, 20, 30), 100)
		self.assertEqual(super_sum(-1 , 1), 0)

	def test_string_input_returns(self):
		"""
		Tests string input returns 0
		"""

		self.assertEqual(super_sum('string',1 ,4), 0)

	def test_sum_of_items_in_a_list(self):
		"""
		Tests sum of items in a single list
		"""

		self.assertEqual(super_sum([1, 2, 3]), 6)
		self.assertEqual(super_sum([1, 2, 3],[1]), 7)

		
