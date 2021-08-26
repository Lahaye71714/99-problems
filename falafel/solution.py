def falafel(s):
	new_list = list(s)
	hist = {}
	for letter in new_list:
		hist[letter] = hist.get(letter, 0) + 1
        
	odd_count = 0
	for key in hist:
		if hist[key] % 2 != 0:
			odd_count += 1
	
	return odd_count <= 1
