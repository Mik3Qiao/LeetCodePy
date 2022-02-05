from typing import List

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		frontLen, backLen = len(s), len(p)
		
		result = []
		if backLen > frontLen:
			return []
		
		frontArr, backArr = [0] * 26, [0] * 26
		for char in p:
			backArr[ord(char) - ord("a")] += 1
		
		for i in range(frontLen):
			frontArr[ord(s[i]) - ord("a")] += 1
			if i >= backLen:
				frontArr[ord(s[i - backLen]) - ord("a")] -= 1
			
			if frontArr == backArr:
				result.append(i - backLen + 1)
		return result
	
	
def run():
	s1, p1 = "cbaebabacd", "abc"
	s2, p2 = "abab", "ab"
	solution = Solution()
	if (solution.findAnagrams(s1, p1) == [0, 6]) and (solution.findAnagrams(s2, p2) == [0, 1, 2]):
		print("Day2 success")
	else:
		raise RuntimeError("Day 2 failed")
	