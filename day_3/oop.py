class Person:
	# class variables
	people_count = 0

	def __init__(self, name, age):
		# instance variables
		self.name = name
		self.age = age
		Person.people_count +=1

	def __repr__(self):
		return "<object: {}, {}> ".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I'm {} and {} y/o".format(self.name, self.age)


p = Person('joe', 23)
p2 = Person('jane', 23)
p3 = Person('George', 49)

print p.say_hello()

a =[('joe', 23),('jane', 26),('jackie', 29),('jee', 20),('josh', 43),('Jacob', 34)]

b = []

for name , age in a:
	person = Person(name, age)
	b.append(person)

for person in b:
	print person.say_hello()

print b
print p.name 
print p.age
print Person.people_count
print p2.people_count
