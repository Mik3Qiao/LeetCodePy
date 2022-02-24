# from typing import List
#
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dict = {}
#         for i in nums:
#             if dict.get(i) is not None:
#                 dict[i] = dict[i] + 1
#             else:
#                 dict[i] = 1
#             if dict[i] > len(nums) / 2:
#                 return i
#

# Definition for singly-linked list.
# from typing import Optional
#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def getMid(headNode: ListNode) -> ListNode:
#     midPrev = None
#     while(headNode is not None) and (headNode.next is not None):
#         if midPrev is None:
#             midPrev = headNode
#         else:
#             midPrev = midPrev.next
#
#         headNode = headNode.next.next
#
#
#     mid = midPrev.next
#     midPrev.next = None
#     return mid
#
#
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if (head is None) or (head.next is None):
#             return head
#
#         mid = getMid(head)
#         left = self.sortList(head)
#         right = self.sortList(mid)
#         return self.merge(left, right)
#
#
#     def merge(self, list1, list2):
#         dummyHead = ListNode()
#         tail = dummyHead
#
#         while()


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        result = self.isSameTree(p.left, p.right) and self.isSameTree(q.left, q.right)
        return result