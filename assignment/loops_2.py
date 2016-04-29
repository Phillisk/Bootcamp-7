b = [(2, 4),(5, 10, 16),(6, 20), (50, 50, 60)]
	
'''
	x: y: z:
	x: y:
'''

for i in b:
	x = len(i)
	if x > 2:
		print "x: {}, y: {}, z: {}".format(i[0], i[1], i[2])
	else:
		print "x: {}, y: {}".format(i[0], i[1])


def vary_loops(*args):
	result = 0
	for item in args:
		if len(item) == 1:
			for x in item:
				result = "x: {}".format(x)
		elif len(item) == 2:
			for x, y in item:
				result = "x: {}, y:{}".format(x, y)
		else:
			len(item) == 3
			for x, y, z in item:
				result = "x: {}, y:{}, z:{}".format(x, y, z)
	return result

print vary_loops([(10,20,40), (23,45), (23,45,67)])

