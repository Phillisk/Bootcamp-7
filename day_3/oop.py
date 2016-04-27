from person import Person
from kenyan import Kenyan
# PEP8
# Instance vs class variables
# class methods

p = Person('joe', 23)
print p


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


k = Kenyan('Miguna', 23)

k.probe(True)
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()

print k.corrupt
