""" 226. Invert Binary Tree
    Author: Artur Gasparyan
    Date: 14 Jan 2023
    Link: https://leetcode.com/problems/invert-binary-tree/submissions/877946486/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root] if root else None

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)

        return root