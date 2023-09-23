# Lowest Common Multiple
from index import factors

# merges common numbers between two arrays and adds unique numbers
# eg: merge([1, 2, 3], [1, 3, 3, 4]) => [1, 2, 3, 3, 4]
def merge(nums1, nums2):
	merged = []
	i, j = 0, 0

	while i < len(nums1) or j < len(nums2):
		if i >= len(nums1):
			merged.append(nums2[j])
			j += 1
		elif j >= len(nums2):
			merged.append(nums1[i])
			i += 1
		elif nums1[i] < nums2[j]:
			merged.append(nums1[i])
			i += 1
		elif nums1[i] > nums2[j]:
			merged.append(nums2[j])
			j += 1
		else:
			merged.append(nums1[i])
			i, j = i+1, j+1

	return merged

# find the LCM by sequentially merging factors of each number
def lcm(nums):
	merged_factors = []
	
	for num in nums:
		merged_factors = merge(factors(num), merged_factors)

	# transform reduce the array with multiplication
	product = 1
	for factor in merged_factors:
		product = product * factor

	return product

print(lcm([1, 2, 3, 4, 5, 10]))		

	
