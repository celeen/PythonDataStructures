import unittest
from main.list import List
from main.empty_exception import EmptyException

class WithNothingAdded(unittest.TestCase):

	def setUp(self):
		self.list = List()

	def test_list_is_empty_initially(self):
		self.assertEqual(self.list.is_empty(), True, "List is not empty initially")

	def test_can_insert_items_at_zero(self):
		self.list.insert(12)
		print self.list.storage
		self.assertEqual(self.list.at(0), 12)

	def test_exception_is_raised_when_accessing_out_of_bounds(self):
		with self.assertRaises(EmptyException):
			self.list.at(1)

	def test_exception_is_raised_when_updating_out_of_bounds(self):
		with self.assertRaises(EmptyException):
			self.list.at(1, 42)

	def test_exception_is_raised_when_removing_out_of_bounds(self):
		with self.assertRaises(EmptyException):
			self.list.remove_at(1)

	def test_exception_is_raised_when_inserting_out_of_bounds(self):
		with self.assertRaises(EmptyException):
			self.list.insert(42, 1)

class AfterAddingAnItem(unittest.TestCase):

	def setUp(self):
		self.list = List()
		self.list.append(42)

	def test_is_not_empty(self):
		self.assertFalse(self.list.is_empty())

	def test_contains_one_item(self):
		self.assertTrue(self.list.size() == 1)

	def test_can_access_the_value(self):
		self.assertEqual(self.list.at(0), 42, "")

class WithSeveralItems(unittest.TestCase):

	def setUp(self):
		self.list = List()
		self.list.append(42).append(2).append(5).append(12)

	def test_list_is_not_empty(self):
		self.assertFalse(self.list.is_empty())

	def test_list_contains_four_items(self):
		self.assertEqual(self.list.size(), 4)

	def test_can_access_list_values(self):
		self.assertEquals(self.list.at(0), 42)
		self.assertEquals(self.list.at(1), 2)
		self.assertEquals(self.list.at(2), 5)
		self.assertEquals(self.list.at(3), 12)

	def test_can_update_list_values(self):
		self.list.at(0, 1)
		self.assertEquals(self.list.at(0), 1)

	def test_can_remove_list_values_moving_subsequent_ones_down(self):
		self.list.remove_at(1)
		self.assertEquals(self.list.at(1),5)

class AfterInsertingAnItem(unittest.TestCase):
	
	def setUp(self):
		self.list = List()
		self.list.append(1).append(2).append(5).append(12)		
		self.list.insert(42, 2)

	def test_list_has_additional_item(self):
		self.assertEqual(self.list.size(), 5)

	def test_new_list_item_is_in_the_right_position(self):
		self.assertEqual(self.list.at(2), 42)

	def test_insertion_moved_previous_value_forward(self):
		self.assertEqual(self.list.at(3), 5)