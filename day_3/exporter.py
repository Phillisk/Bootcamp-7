people =[('joe', 23),('jane', 26),('jackie', 29),('jee', 20),('josh', 43),('Jacob', 34)]

def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {} and {} years old".format(name, age)

def max_min(A):
	'''
	Returns max value - min value
	e.g a =[10, 40, -5, 6, 9, 34, 7]

	'''
	#return max(A) - min(A)

	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i

	return max_ - min_


