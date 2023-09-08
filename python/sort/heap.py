import numbers as n

def heap (nums):
	def swap (i, j):
		nums[i], nums[j] = nums[j], nums[i]

	def heapify (i, end):
		left = lambda i: (i * 2) + 1
		right = lambda i: (i * 2) + 2

		while left(i) < end:
			max = left(i)
			if right(i) < end and nums[right(i)] > nums[left(i)]:
				max = right(i)
			if nums[i] < nums[max]:
				swap(i, max)
				i = max
			else:
				break

	# heapify input array
	for i in range(len(nums) - 1, -1, -1):
		heapify(i, len(nums))

	# sort by polling from the heap
	for i in range(len(nums)):
		peek = nums[0]
		nums[0] = nums[len(nums) - i - 1]
		heapify(0, len(nums) - i - 1)
		nums[len(nums) - i - 1] = peek

	return nums


n.test_sort(heap)
