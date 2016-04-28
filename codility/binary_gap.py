def solution(N):
	'''
	Takes an positive integer N:
		- gets its binary representation
		- determines the binary gap(s)
		- returns the longest binary gap.
		e.g. given N = 1041 the function should return 5, 
		because N has binary representation 10000010001 and 
		so its longest binary gap is of length 5.
	'''
	count = 0
	result = 0
	one = False
	i = N

	while i:
		if i & 1 == 1:

			if one == False:
				one = True
				
			else:
				result = max(result,count)
			count = 0
		else:
			count += 1
		i >>= 1
	return result


print solution(1041)
