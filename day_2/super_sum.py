def super_sum(A):
	'''
	Takes a list of numbers(A), and:
		halves the even numbers
		mdoubles the odd numbers
	then returns the sum of all
	
	'''
	total = 0

	for i in A:
		if i % 2 == 0:
			total += (i / 2)
		else:
			total += (i * 2)
	
	return total



