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

def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) = 30
		super_sum(10, 20, 40) = 70
		super_sum(1, 2, 3, 4, 5) = 15
	'''
	total = 0
	for i in args:
		total += i

	return total

print super_sum(10, 20)
print super_sum(1, 4, 7, 5)
a = [10, 40, 60]
print super_sum(*a)


def hello_again(**kwargs):
	return "I am {}, and I'm {} y/o".format(kwargs['name'], kwargs['age'])

print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')

joe = {'name': 'Joe', 'age': 28}
print hello_again(**joe)
print hello_again(name='joe', age = 28)