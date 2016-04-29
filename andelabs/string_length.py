def string_length(data):
	b = []

	if type(data) == str:
		b.append(len(data))
		return b
		
	elif type(data) == list:
		for item in data:
			b.append(len(item))
	return b

