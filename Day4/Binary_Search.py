'''BinarySearch class inheriting from List and having a search function(recursive) containing an argument'''
class BinarySearch(list):
	def __init__(self, a, b):
		'''a is the lenght of the list and b is the step or difference between consecutive values'''
		self.a = a
		self.b = b

	def search(self, search_value):
		'''Initializing the counter value'''
		counter = 0
		
		'''Initialize lower_index to 0'''
		lower_index = 0

		'''index of last element in the current search list'''
		higher_index = self.a - 1
		'''Using divide and conquer algorithm to search for the value'''
		'''index of midpoint element'''
		midpoint_value= lower_index + (higher_index - lower_index)//2

		if search_value == midpoint_value:
			'''incrementing counter and return dictionary of counter(key) and index of element(value)'''
			counter = counter + 1
			return {counter: midpoint_value}
		elif search_value > midpoint_value:
			'''Element is to be found in upper bound of list'''
			lower_index = midpoint_value + 1
			midpoint_value = lower_index + (higher_index - lower_index)//2
			self.search(search_value)
		elif search_value < midpoint_value:
			higher_index = midpoint_value - 1
			midpoint_value = lower_index + (higher_index - lower_index)//2
			self.search(search_value)
