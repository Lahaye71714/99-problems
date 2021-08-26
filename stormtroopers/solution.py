def stormtroopers(numbers):
	hist = {}
	for x in numbers:
		hist[x] = hist.get(x, 0) + 1
	new_list = [x for x in hist if hist[x] == 1]
	return new_list
