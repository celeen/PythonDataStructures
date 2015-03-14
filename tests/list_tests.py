import unittest 
from main.list import MetaList
from main.custom_exceptions import *

class MetaListTests(unittest.TestCase):
	
	def setUp(self):
		self.list = MetaList()
		self.list = MetaList(4,5,6)

	def test_is_empty(self):
		self.assertEqual(self.list.is_empty(), False)

	def test_getter(self):
		pass

		# insert can insert an item anywhere in the list, moving 
	def test_setter(self):
		self.list[0] = 3
		self.assertEqual(self.list[0], 3)

	def test_insert_with_one_argument(self):
		# insert automatically inserts an item at the end
		self.list.insert(1)
		self.assertEqual(self.list[0], 1)

	def test_insert_with_two_arguments(self):
		self.list.insert(3, 1)
		self.assertEqual(self.list[1], 3)
		self.assertEqual(self.list.storage, [4,3,5,6])

	def test_append(self):
		self.list.append(7)
		self.assertEqual(self.list[-1], 7)

		self.assertEqual(self.list.storage, [4,5,6,7])

	def test_extend(self):
		self.list.extend([7,8,9])
		self.assertEqual(self.list.storage, [4,5,6,7,8,9])

	def test_remove(self):
		self.list.remove(5)
		self.assertEqual(self.list.storage, [4,6])

	def test_naked_pop(self):
		self.list.pop()
		self.assertEqual(self.list.storage, [4,5])

	def test_clothed_pop(self):
		self.list.pop(1)
		self.assertEqual(self.list.storage, [4,6])

	def test_index(self):
		self.assertEqual(self.list.index(6), 2)

		with self.assertRaises(ItemNotFound):
			self.list.index(42)

		self.list.append(6)
		self.assertEqual(self.list.index(6), 2)

	def test_count_with_one_of_each(self):
		self.assertEqual(self.list.count(4), 1)

		self.list.append(4)
		self.assertEqual(self.list.count(4), 2)

	def test_sort(self):
		self.list.append(0)
		self.list.sort()

		self.assertEqual(self.list.storage, [0,4,5,6])

	def test_reverse(self):
		self.assertEqual(False, True)