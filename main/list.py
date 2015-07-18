import __future__
from .custom_exceptions import *

class MetaList:
	def __init__(self, *starting_values):
		if not starting_values:
			print "HELLO:"
			print starting_values
			self.storage = []
		else:
			self.storage = list(starting_values)

	def __getitem__(self, index):
		return self.storage[index]

	def __setitem__(self, index, value):
		self.storage[index] = value

	def size(self):
		return len(self.storage)

	def is_empty(self):
		return not self.storage

	def at(self, position, put=None):
		# self.empty_check(position)
		if put is not None:
			self.storage[position] = put

		return self.storage[position]

	def insert(self, position, item):
		# self.empty_check(position)
		self.storage.insert(position, item)

	def append(self, x):
		self.insert(len(self.storage), x)
		return self

	def extend(self, extension):
		for item in extension:
			self.storage.append(item)

		return self.storage

	def remove(self, x):
		self.storage.remove(x)

	def pop(self, index=None):
		if index:
			number = self[index]
			new_list = self.storage[:index] + self.storage[index+1:]
			self.storage = new_list
			return number
		else:
			number = self[-1]
			self.storage = self.storage[0:-1]
			return number


		# self.storage.remove(self[index])

	def index(self, x):
		for i in range(self.size()):
			if self[i] == x:
				return i
		else:
			raise ItemNotFound

	def count(self, x):
		instances = 0
		for item in self:
			if item == x:
				instances += 1

		return instances

	#  -----------BONUS---------------

	def sort(self):
		for i in range(1, self.size()):
			j = i
			while j > 0 and self[j] < self[j - 1]:
				self[j], self[j - 1] = self[j - 1], self[j]
				j -= 1

		return self

	def reverse(self):
		j = self.size() - 1

		for i in range(self.size()):
			if j - i >= 1:
				self[i], self[j] = self[j], self[i]
			j -= 1

		return self


