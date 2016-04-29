def words(A):
	'''
	takes in a sentence:
	and returns the words in it an the number of times they occur
	For example for the input "olly olly in come free"

	olly: 2
	in: 1
	come: 1
	free: 1
	'''	

	a = A.split()
	
	# initialize an empty dictionary
	dict1 = {}
	b = len(a) 

	for i in a:
		if i.isdigit():
			i = int(i)
			
		if i in dict1:
			dict1[i] = a.count(i)
		else:
		    dict1[i] = 1
		    
	return dict1


# print words("he he went there he")
# print words("he he went 2 he 2 yes no yes")
print words('testing 1 2 testing')
