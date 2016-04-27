def hello(name, age, class_ = ''):
	'''
	Implemention of args and kwargs
	'''
	if class_ != '':
		return "I am {}, I'm {} y/o and {} class".format(name, age, class_)
	return "I am {}, and I'm {} y/o".format(name, age)

people = [
			("Jane", 23, 'High'),
			("Joe", 25, 'Low'),
			("Brian", 60),
			("Betty",45)
			]

# for name, age, class_ in people:
# 	print hello(name, age, class_)

# use of unpacking

for person in people:
	print hello(*person)
