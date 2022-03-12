# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]

        return None

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node is not None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]



        # if not head:
        #     return head
        #
        # ptr = head
        # while ptr:
        #     duplicate = Node(ptr.val, None, None)
        #     duplicate.next = ptr.next
        #     ptr.next = duplicate
        #     ptr = duplicate.next
        #
        # ptr = head
        # while ptr:
        #     ptr.next.random = ptr.random.next if ptr.random else None
        #     ptr = ptr.next.next
        #
        # ptr_old_list = head
        # ptr_new_list = head.next
        # head_new = head.next
        # while ptr_old_list:
        #     ptr_old_list.next = ptr_old_list.next.next
        #     ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
        #     ptr_old_list = ptr_old_list.next
        #     ptr_new_list = ptr_new_list.next
        # return head_new

