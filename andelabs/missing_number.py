def find_missing(A, B):
  """
  You are presented with two arrays, all containing positive integers. 
  One of the arrays will have one extra number, see below:
  
  [1,2,3] and [1,2,3,4] should return 4
  
  [4,66,7] and [66,77,7,4] should return 77
  
  """
  
  if A != B:
    set1 = set(A)
    set2 = set(B)

    if set1 != set2:
      x = set2 - set1
      b = list(x)
      return b[0]

  return 0
 

print find_missing([1,2,3],[1,2,3,5])

list1 = find_missing([1, 2], [1, 2, 5])
list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
print [list1, list2, list3]


