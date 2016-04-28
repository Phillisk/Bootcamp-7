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

