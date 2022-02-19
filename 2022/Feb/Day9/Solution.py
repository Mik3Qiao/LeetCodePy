# from typing import List
#
# class Solution:
# 	def minimumDeviation(self, nums: List[int]) -> int:
# 		localMin, localMax = self.findMinMax(nums)
# 		for i in nums:
# 			if localMin < i < localMax:
# 				if i % 2 == 0:
#
#
#
# 	def findMinMax(self, numArr: List[int]) -> (int, int):
# 		min = float('inf') - 1
# 		max = float('-inf') + 1
# 		for i in numArr:
# 			if min > i:
# 				min = i
# 			elif max < i:
# 				max = i
#
# 		return (min, max)

from typing import Optional
class ListNode:
	def __init__(self, val=0, next = None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		addition = 0
		head = ListNode(0)
	
		curr = head
	
		while l1 is not None or l2 is not None:
			l1Value = l1.val if l1 is not None else 0
			l2Value = l2.val if l2 is not None else 0
			
			value = l1Value + l2Value + addition
			remainder = value % 10
			addition = int((value - remainder) / 10)
			
			curr.next = ListNode(remainder)
			curr = curr.next
			
			if l1 is not None:
				l1 = l1.next
			if l2 is not None:
				l2 = l2.next
	
		if addition > 0:
			curr.next = ListNode(addition)
	
		return head.next
		