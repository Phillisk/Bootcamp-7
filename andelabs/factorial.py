def factorial(number):
  """
  Takes the number parameter been passed and return the factorial of it.
  """
  if number == 0:
    return 1
  return number * factorial(number-1)

print factorial(2)