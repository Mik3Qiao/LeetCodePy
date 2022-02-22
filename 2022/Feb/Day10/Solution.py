from typing import List
# class Solution:
# 	def titleToNumber(self, columnTitle: str) -> int:
# 		result = 0
#
# 		for i in range(len(columnTitle)):
# 			result = result * 26
# 			result += ord(columnTitle[i]) - ord('A') + 1
#
# 		return result

class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key = lambda x: (x[0], -x[1]))
		count = 0
		
		end, prevEnd = 0, 0
		for i in range(len(intervals)):
			end = intervals[i][1]
			if prevEnd < end:
				prevEnd = end
				count += 1
				
		return count