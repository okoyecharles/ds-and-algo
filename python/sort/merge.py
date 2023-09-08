import numbers as n

def merge(nums):
	def swap(i, j):
		nums[i], nums[j] = nums[j], nums[i]

	def merge_nums(l, mid, r):
		a = nums[l : mid + 1]
		a.append(float('inf'))
		b = nums[mid + 1 : r + 1]
		b.append(float('inf'))
		i, j, k = 0, 0, l

		while k <= r:
			if a[i] < b[j]:
				nums[k] = a[i]
				i = i + 1
			else:
				nums[k] = b[j]
				j = j + 1
			k = k + 1
			
	def merge_sort(l = 0, r = len(nums) - 1):
		if l < r:
			mid = int((l + r) / 2)
			merge_sort(l, mid)
			merge_sort(mid + 1, r)
			merge_nums(l, mid, r)

	merge_sort()
	return nums

n.test_sort(merge)

