from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # checked = set()
        # while head is not None:
        #     if head in checked:
        #         return True
        #     checked.add(head)
        #     head = head.next
        # return False
        if head is None:
            return False
        left = head
        right = head.next
        while left != right:
            if right is None or right.next is None:
                return False
            left = left.next
            right = right.next.next

        return True
