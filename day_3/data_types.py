def data_type(x):
	'''
	Takes in an argument, x:
		- For an integer, return x**2
		- For a float, return x/2
		- For a string, return "Hello " + x
		- For a boolean, return boolean
		- For a long, return squareroot(x)
	'''

	if  type(x) == int:
		return x**2
	elif type(x) == float:
		return x/2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	
	return "Input is not an int, float, boolean, string or long"

# print data_type(2)
# print data_type('World')	
# print data_type(10.0)
# print data_type(True)
# print data_type(50**50)
# print data_type(None)
# print data_type('Phillis')




