import numbers as n

def selection(nums):
	def swap(i, j):
		nums[i], nums[j] = nums[j], nums[i]

	for sorted_end in range(len(nums) - 1):
		min_index = len(nums) - 1 
		for i in range(sorted_end, len(nums)):
			if nums[i] < nums[min_index]:
				min_index = i
		swap(sorted_end, min_index)

	return nums

n.test_sort(selection)
