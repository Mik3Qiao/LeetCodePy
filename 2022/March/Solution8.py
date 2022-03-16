# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        counter = 1
        dummy_head = head
        while dummy_head.next:
            dummy_head = dummy_head.next
            counter += 1

        dummy_head.next = head

        for i in range(counter - k % counter - 1):
            tail = tail.next

        new_head = tail.next
        tail.next = None

        return new_head

    # class Solution:
    #     def isValid(self, s: str) -> bool:
    #         localStack = []
    #         for i in s:
    #             if i == "(" or i == "[" or i == "{":
    #                 localStack.append(i)
    #             elif i == ")" or i == "]" or i == "}":
    #                 if len(localStack) == 0:
    #                     return False
    #                 lastone = localStack.pop()
    #                 if lastone == "(" and i == ")" or lastone == "[" and i == "]" or lastone == "{" and i == "}":
    #                     continue
    #                 else:
    #                     return False
    #
    #         if len(localStack) == 0:
    #             return True
    #         else:
    #             return False