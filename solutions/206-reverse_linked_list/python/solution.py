""" 206. Reverse Linked List
    Author: Artur Gasparyan
    Date: 19 Jan 2023
    Link: https://leetcode.com/problems/reverse-linked-list/submissions/881086776/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        if not head:
            return

        new_head = None

        while head:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp

        return new_head
