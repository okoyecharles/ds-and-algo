# Highest Common Factor

from index import factors

# returns all common values between two sorted arrays
# eg: intersect([1, 2, 3], [2, 3, 5]) => [2, 3]
def intersect(nums1, nums2):
        intersected = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                        i += 1
                elif nums1[i] > nums2[j]:
                        j += 1
                else:
                        intersected.append(nums1[i])
                        i, j = i+1, j+1

        return intersected

# finds the hcf by sequentially finding all common factors between numbers
def hcf(nums):
	# assign to first number's factors
	common_factors = factors(nums[0])
	
	for num in nums:
		if len(common_factors) == 0: return 1
		common_factors = intersect(factors(num), common_factors)
	
	# transform reduce factors with multiplication
	product = 1
	for factor in common_factors:
		product = product * factor

	return product

print(hcf([729, 336, 900]))
