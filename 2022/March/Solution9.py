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

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.result += root.val
                if low < root.val:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)

        self.result = 0
        dfs(root)
        return self.result
