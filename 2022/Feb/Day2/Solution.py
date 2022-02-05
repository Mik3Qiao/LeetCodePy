from typing import List
from collections import Counter

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		frontlen, backlen = len(s), len(p)
		result = []

		if backlen > frontlen:
			return result
		
		backCounter = Counter(p)
		frontCounter = Counter()

		for i in range(frontlen):
			frontCounter[s[i]] += 1
			
			if i >= backlen:
				if frontCounter[s[i - backlen]] == 1:
					del frontCounter[s[i-backlen]]
				else:
					frontCounter[s[i-backlen]] -= 1
					
			if frontCounter == backCounter:
				result.append(i - backlen + 1)
		
		return result
	
	def findAnagrams2(self, s: str, p: str) -> List[int]:
		frontLen, backLen = len(s), len(p)
		
		result = []
		if backLen > frontLen:
			return []
		
		frontArr, backArr = [0]*26, [0]*26
		for char in p:
			backArr[ord(char) - ord("a")] += 1
			
		for i in range(frontLen):
			frontArr[ord(s[i]) - ord("a")] += 1
			if i >= backLen:
				frontArr[ord(s[i-backLen]) - ord("a")] -= 1
			
			if frontArr == backArr:
				result.append(i - backLen + 1)
		return result

s = "cbaebabacd"
p = "abcaaa"

# s = "abab"
# p = "ab"

solution = Solution()
# print(solution.findAnagrams(s, p))
