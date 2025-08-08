def compression(s):
	cur = 0
	count = 0
	pre = ''
	t = ''
	for c in s:
		if pre == '':
			count += 1
			t += c
			pre = c
		elif c == pre :
			count += 1
			pre = c
		else:
			t += str(count)
			t += c
			count = 1
			pre = c
	t += str(count)
	print t
	if (len(s) > len(t)):
		return t
	else:
		return s

	
