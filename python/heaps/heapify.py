def heapify (nums):
	def heapify_down (index):
		curr = index
		left, right = (curr*2)+1, (curr*2)+2
		
		while left < len(nums):
			max = left
			if right < len(nums) and nums[right] > nums[left]:
				max = right
			if nums[curr] > nums[max]:
				break
			temp = nums[curr]
			nums[curr] = nums[max]
			nums[max] = temp
			curr = max
			left, right = (curr*2)+1, (curr*2)+2
		
	for i in range(len(nums) - 1, -1, -1):
		heapify_down(i)

nums = [3,4,5,2,98,10,2,4]
heapify(nums)
print(nums)
