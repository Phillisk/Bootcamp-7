def arith_geo(A):
  """
  You are required to check if the array passed as an argument is arithmetic, geometric, neither arithmetic nor geometric in progression or if the array is empty.

      -For arithmetic progressions, return Arithmetic
      -For geometric progressions, return Geometric
      -For neither of the above, return -1
      -For an empty array, return 0
  """
  x = len(A)
  
  if x == 0:
    return 0
    
  for i in range(x - 1):
    if A[i+1] - A[i] == A[i+2] - A[i+1] == A[i+3] - A[i+2]:
      return "Arithmetic"
    
    elif A[i+1] / A[i] == A[i+2] / A[i+1] == A[i+3] / A[i+2]:
      return "Geometric"
      
    else:
      return -1
    