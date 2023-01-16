""" 235. Lowest Common Ancestor of a Binary Tree
    Author: Artur Gasparyan
    Date: 16 Jan 2023
    Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/879196209/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def construct_path(node, parents):
    path = set()

    while node:
        path.add(node)
        node = parents[node]

    return path

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:None}
        frontier = [root]

        path_to_p = None
        path_to_q = None

        while True:
            node = frontier.pop()
            if node.left:
                frontier.append(node.left)
                parents[node.left] = node

            if node.right:
                frontier.append(node.right)
                parents[node.right] = node

            if node == p:
                path_to_p = construct_path(node, parents)
                if path_to_q:
                    break

            elif node == q:
                path_to_q = construct_path(node, parents)
                if path_to_p:
                    break


        common_path = path_to_p.intersection(path_to_q)
        
        node = p
        while True:
            if node in common_path:
                return node

            node = parents[node]

        return None
            