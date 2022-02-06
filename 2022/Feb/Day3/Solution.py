from typing import List


class Solution:
	def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
		# Brute force solution is obviously not feasible here...
		
		# for i in nums1:
		# 	if (nums1[i] >= 0) and (nums2[i] >= 0) and (nums3[i] >= 0) and (nums4[i] >= 0):
		# 		return 0
		
		dict = {}
		count = 0
		
		for i in nums1:
			for j in nums2:
				if i+j in dict:
					dict[i + j] += 1
				else:
					dict[i+j] = 1
				
		for k in nums3:
			for l in nums4:
				if -(k+l) in dict:
					count += 1
		
		return count
		
		
def run():
	nums1 = [1, 2]
	nums2 = [-2, -1]
	nums3 = [-1, 2]
	nums4 = [0, 2]
	solution = Solution()
	if solution.fourSumCount(nums1, nums2, nums3, nums4) == 2:
		print("Day3 success")
	else:
		raise RuntimeError("Day3 failed")

# nums1 = [0]
# nums2 = [0]
# nums3 = [0]
# nums4 = [0]

# solution = Solution()
# print(solution.fourSumCount(nums1, nums2, nums3, nums4))

	
