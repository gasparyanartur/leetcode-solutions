""" 141. Linked List Cycle
    Author: Artur Gasparyan
    Date: 17 Jan 2023
    Link: https://leetcode.com/problems/linked-list-cycle/submissions/879873679/ 
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False