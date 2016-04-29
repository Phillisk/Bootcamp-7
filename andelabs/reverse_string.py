
def reverse_string(string):
	"""
	returns the reverse of the string provided. 
	If the reverse of the string is the same as the original string, 
	as in the case of palindromes, return true instead

	"""
	x = len(string)
	b = []

	for i in range(x-1, -1, -1):
		b.append(string[i])
		string1 = "".join(b)

	if string == "":
	  return None
	elif b == list(string):
		return True
	else:
		return string1

print reverse_string("phil")
print reverse_string("")