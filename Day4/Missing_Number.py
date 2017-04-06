'''Passing the two lists as argument containing numbers'''
def find_missing(list1, list2):
	'''First we  verify that the two passed arguments are lists '''
	if type(list1) and type(list2) is list: 
		if list1 == list2:
			'''Testing whether the two arguments are equal if so zero will be returned'''
			print(0)
		else:
			'''use data type set to get the difference between the two lists and save it to a list'''

			get_missing_number = list(set(list2) - set(list1))

			'''get_missing_number is a list, use index to get the element'''
			print(get_missing_number[0])
	else:
		'''If arguments passed are not lists'''
		print('Only list arguments required')
#find_missing([1, 2], [1, 2, 5]) gives 5
