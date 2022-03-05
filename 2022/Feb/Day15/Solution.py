# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         left, right = len(s), len(t)
#
#         p_left = p_right = 0
#
#         while p_left < left and p_right < right:
#             # move both pointers or just the right pointer
#             if s[p_left] == t[p_right]:
#                 p_left += 1
#             p_right += 1
#
#         return p_left == left


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy
        for i in range(n+1):
            right = right.next

        while right is not None:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next