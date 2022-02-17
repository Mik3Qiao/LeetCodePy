from typing import List


class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		results = []
		
		def backtrack(remain, comb, start):
			if remain == 0:
				results.append(list(comb))
				return
			elif remain < 0:
				return
			
			for i in range(start, len(candidates)):
				comb.append(candidates[i])
				backtrack(remain - candidates[i], comb, i)
				comb.pop()
		
		backtrack(target, [], 0)
		return results

# class Solution:
# 	def subarraySum(self, nums: List[int], k: int) -> int:
# 		sum = 0
# 		count = 0
# 		newDict = {}
# 		newDict[0] = 1
#
# 		for i in range(len(nums)):
# 			sum += nums[i]
# 			if (newDict.has_key(sum - k)):
# 				count += newDict[sum - k]
# 			newDict[sum] = newDict.get(sum, 0) + 1
#
# 		return count


# result = 0
# for start in range(0, len(nums)):
# 	sum = 0
# 	for end in range(start, len(nums)):
# 		sum += nums[end]
# 		if sum == k:
# 			result += 1
#
# return result
