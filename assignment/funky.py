def funky(a, b):
	'''
	print out the sum two numbers

	'''

	if type(a) == int and type(b) == int:
		print (a + b)
		
	elif type(a) == float and type(b) == float:
		print a + b

	elif type(a) == str and type(b) == str:
		print a + b

	elif type(a) == list and type(b) == list:
		print a + b

	elif type(a) == dict and type(b) == dict:
		print dict(a.items() + b.items())
	
	else:
		type(a) != type(b)
		print "Invalid Input"

funky(10, 20)
funky(10.2, 20.3)
funky({'one': 10, 'two': 20}, {1: 'one', 2: 'two'})
funky('10', '20')
funky([10, 20], [12, 3, 4])
funky(10, '20')
funky('phil', 20)		