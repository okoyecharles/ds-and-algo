def allConstruct(target, bank):
	table = [[] for i in range(len(target) + 1)]
	table[0] = [[]]

	for i in range(len(table)):
		if len(table[i]) > 0:
			for word in bank:
				if i + len(word) > len(target): continue
				prefix = target[i: i + len(word)]
				if prefix == word:
					for comb in table[i]:
						new_comb = comb + [word]
						table[i + len(word)].append(new_comb)
				 
	return table[len(target)]

print(allConstruct('abcdef', ['ab', 'abc', 'c', 'def', 'abcd']))
