import numbers as n

def quick(nums):
	nums.append(float('inf'))
	def swap(i, j):
		nums[i], nums[j] = nums[j], nums[i]

	def partition(l, r):
		p = l
		i, j = l, r
		while i < j:
			while not nums[i] >= nums[p]:
				i = i + 1
			while j > p and not nums[j] < nums[p]:
				j = j - 1

			if i < j:
				swap(i, j)
		swap(j, p)
		return j
		

	def quick_sort(l = 0, r = len(nums) - 1):
		if l < r:
			p = partition(l, r)
			quick_sort(l, p)
			quick_sort(p + 1, r) 
	quick_sort()
	nums.pop()
	return nums
		

n.test_sort(quick)
