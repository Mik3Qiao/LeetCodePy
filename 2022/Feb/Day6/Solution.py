import collections
from collections import defaultdict
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         newHead = ListNode(-1)
#         newHead.next = head
#
#         prevNode = newHead
#
#         while head and head.next:
#             firstNode = head
#             secondNode = head.next
#
#             prevNode.next = secondNode
#             firstNode.next = secondNode.next
#             secondNode.next = firstNode
#
#             prevNode = firstNode
#             head = firstNode.next
#
#         return newHead.next

#     subsets
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
#         for number in nums:
#             for i in result:
#                 result = result + [i + [number]]
#         return result

# Permutation in string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1Arr = [0] * 26
            s2Arr = [0] * 26
            
            for i in range(len(s1)):
                s1Arr[ord(s1[i]) - ord("a")] += 1
                s2Arr[ord(s2[i]) - ord("a")] += 1
                
            output = False
            for i in range(len(s2) - len(s1)):
                if s1Arr == s2Arr:
                    output = True
                else:
                    s2Arr[ord(s2[i+len(s1)]) - ord('a')] += 1
                    s2Arr[ord(s2[i]) - ord('a')] -= 1

            if s1Arr == s2Arr:
                output = True
            return output
            