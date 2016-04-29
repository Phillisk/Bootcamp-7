def find_max_min(a):
  """
  Returns an array containing min amd max number resp.
  If max = min return length(a)
  """

  if type(a) == list:
    min_ = min(a)
    max_ = max(a)
    if min_ != max_:
      return [min_ , max_]
    
    else:
      return [len(a)]
  else:
  	pass


x = find_max_min([1, 2, 3, 4])
y = find_max_min([4, 4, 4, 4, 4])
print x , y
