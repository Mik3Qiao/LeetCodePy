from typing import List, Optional


# class Solution:
#     def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
#         top = {}
#         bottom = {}
#         common = {}
#
#         for i in tops:
#             if i not in top:
#                 top[i] = 1
#             else:
#                 top[i] += 1
#
#         for i in bottoms:
#             if i not in bottom:
#                 bottom[i] = 1
#             else:
#                 bottom[i] += 1
#
#         for i in tops:
#             if tops[i] == bottoms[i]:
#                 if tops[i] not in common:
#                     common[i] = 1
#                 else:
#                     common[i] += 1
#
#         countA = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#         countB = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#         same = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#         for i in range(len(tops)):
#             countA[tops[i]] += 1
#             countB[bottoms[i]] += 1
#             if tops[i] == bottoms[i]:
#                 same[tops[i]] += 1
#
#         for j in range(1, 7):
#             if (countA[j] + countB[j] - same[j] == len(tops)):
#                 return len(tops) - max(countA[j], countB[j])
#
#         return -1

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        head.next = list1 or list2
        return
