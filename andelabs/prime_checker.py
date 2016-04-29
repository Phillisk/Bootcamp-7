class PrimeChecker(object):
  """
  Takes in a string argument. 
  When the instance of the class is called with .is_prime() it should return true if number is a prime number 
  and false if it isn't.
  
  """
  def __init__(self, number = None):
    self.number = number
  
  def is_prime(self):
  	if self.number == '':
  		return False

  	if self.number < 2:
  		return False

  	if self.number == 1:
  		return False
  	else:
  		self.number = int (self.number)
  		for i in range(2, self.number + 1):
  			if self.number % i != 0:
  				return True
  			return False

x = PrimeChecker('7')
print x.is_prime()

