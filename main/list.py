from empty_exception import EmptyException

class List:
	def __init__(self):
		self.storage = []

	def size(self):
		return len(self.storage)
	
	def is_empty(self):
		return self.size() == 0

	def insert(self, item, position=0):
		self.empty_check(position)
		self.storage.insert(position, item)

	def at(self, position, put=None):
		self.empty_check(position)

		if put != None:
			self.storage[position] = put

		return self.storage[position]

	def append(self, item):
		self.storage.append(item)
		return self

	def remove_at(self, position=0):
		self.empty_check(position)

		self.storage.remove(self.at(position))

	def empty_check(self, position):
		if position > len(self.storage):
			raise EmptyException
	# more advanced stuff



