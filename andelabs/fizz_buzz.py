def fizz_buzz(x):
	'''
	Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', 
	or the argument it receives, all depending on the argument of the function,
	a number that is divisible by, 3, 5, or both 3 and 5, respectively.

	When the number is not divisible by 3 or 5, the number itself should be returned.
	'''
  
  
	if x%3 == 0 and x%5 == 0:
		return 'FizzBuzz'

	if x%3 == 0:
		return 'Fizz'

	if x%5 == 0:
		return 'Buzz'

	return x
  