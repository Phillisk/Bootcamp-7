def sum_digits(A):
	'''
	Takes a list A, and returns the sum of all
	the digits in the list. e.g. [10, 30, 45]
	should return 1 + 0 + 3 + 0 +4 +5

	'''
	total = 0

	for i in A:

		for j in str(i):
			
			total += int(j)

	return total



