def canConstruct(target, bank):
	table = [False] * (len(target) + 1)
	table[0] = True
	# t f t t t f f

	for i in range(len(table)):
		if table[i] == True:
			suffix = target[i:]
			for word in bank:
				if suffix.find(word) == 0:
					end = i + len(word)
					if end < len(table): table[end] = True
					if end == len(table) - 1: return True

	return table[-1]

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'd', 'ef', 'abcd']))
	
