import numbers as n

def bubble(nums):
	def swap(i, j):
		nums[i], nums[j] = nums[j], nums[i]

	for i in range(len(nums) - 1):
		for j in range(len(nums) - i - 1):
			if nums[j] > nums[j + 1]:
				swap(j, j + 1)
	return nums	

n.test_sort(bubble)
