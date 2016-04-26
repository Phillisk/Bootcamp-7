def super_sum(A):
	'''
	Takes a list of numbers(A), divide the even numbers by 2 and multiply the odd numbers by 2
	then adds the results.
	
	'''
	total = 0

	for i in A:
		if i % 2 == 0:
			total += (i / 2)
		else:
			total += (i * 2)
	
	return total

super_sum([2,3])	


