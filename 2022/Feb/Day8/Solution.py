# class Solution:
# 	def removeKdigits(self, num: str, k: int) -> str:
# 		if k > len(num):
# 			return "0"
# 		arr = []
# 		for i in range(len(num)):
# 			while arr and k and (arr[-1] > num[i]):
# 				arr.pop()
# 				k -= 1
# 			arr.append(num[i])
#
# 		finalStack = arr[:-k] if k else arr
#
# 		return "".join(finalStack).lstrip('0') or "0"

class Solution:
	def addDigits(self, num: int) -> int:
		if num == 0:
			return 0
		if num % 9 == 0:
			return 9
		
		return num % 9
