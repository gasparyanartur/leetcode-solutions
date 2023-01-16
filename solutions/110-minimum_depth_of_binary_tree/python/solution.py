""" 110. Balanced Binary Tree
    Author: Artur Gasparyan
    Date: 16 Jan 2023
    Link: https://leetcode.com/problems/balanced-binary-tree/submissions/879235704/
"""


def get_height(node) -> int:
    if node is None:
        return 0
    
    if (left_height := get_height(node.left)) == -1:
        return -1

    if (right_height := get_height(node.right)) == -1:
        return -1

    if abs(right_height - left_height) > 1:
        return -1

    return 1 + max(right_height, left_height) 


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return get_height(root) != -1