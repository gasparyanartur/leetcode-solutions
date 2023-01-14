""" 226. Invert Binary Tree
    Author: Artur Gasparyan
    Date: 14 Jan 2023
    Link: https://leetcode.com/problems/invert-binary-tree/submissions/877942536/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            stack = [root]
        else:
            stack = []

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    node.left = stack[-1]
                    node.right = stack[-2]
                else:
                    node.right = node.left
                    node.left = None

            else:
                if node.right:
                    stack.append(node.right)
                    node.left = node.right
                    node.right = None

        return root