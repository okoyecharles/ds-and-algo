import numbers as n

def insertion(nums):
	def swap(i, j):
		nums[i], nums[j] = nums[j], nums[i]

	i = 0
	while i < len(nums):
		while i > 0 and nums[i] < nums[i - 1]:
			swap(i, i - 1)
			i = i - 1
		i = i + 1

	return nums

n.test_sort(insertion)

