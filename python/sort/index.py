def sort(vals, predicate = lambda i, j: i < j):
	def merge(s, m, e):
		arr_1, arr_2 = vals[s:m+1], vals[m+1:e+1]
		i, j, k = 0, 0, s

		while i < len(arr_1) or j < len(arr_2):
			if i >= len(arr_1):
				vals[k] = arr_2[j]
				j = j + 1
			elif j >= len(arr_2):
				vals[k] = arr_1[i]
				i = i + 1
			elif predicate(arr_1[i], arr_2[j]):
				vals[k] = arr_1[i]
				i = i + 1
			else:
				vals[k] = arr_2[j]
				j = j + 1
			k = k + 1

	def merge_sort(s, e):
		if s < e:
			mid = (s + e) // 2
			
			merge_sort(s, mid)
			merge_sort(mid+1, e)
			merge(s, mid, e)

	merge_sort(0, len(vals)-1)
	return vals

values = [3, 2, 1, 4, 5, 17, 0.5]
sort(values)

strings = ['hi', 'bow', 'catastrophe', 'o', 'rie', 'ring', 'attic']
sort(strings, lambda a, b: len(a) < len(b))

print(values)
print(strings)
