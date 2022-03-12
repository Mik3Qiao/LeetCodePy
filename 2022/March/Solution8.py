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