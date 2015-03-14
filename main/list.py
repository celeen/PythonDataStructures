from custom_exceptions import *

class MetaList:
	
	def __init__(self, *starting_values):
		if not starting_values:
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

	def insert(self, item, position=0):
		# self.empty_check(position)
		self.storage.insert(position, item)

	def append(self, x):
		self.insert(x, len(self.storage))
		return self

	def extend(self, extension):
		for item in extension:
			self.storage.append(item)

		return self.storage

	def remove(self, x):
		self.storage.remove(x)

	def pop(self, index=-1):
		self.storage.remove(self[index])

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
		# new_list = []
		# for i in range(self.size()):
		# 	if self[i] < self[i+1]:
		# 		new_list.append(self[i])
		pass

	def reverse():
		pass


