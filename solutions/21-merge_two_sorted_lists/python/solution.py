""" Problem 21. Merge Two Sorted Lists
    Author: Artur Gasparyan
    Date: 11 Jan 2023
    Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/876415493/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1

        if not list1:
            return list2

        if list1.val < list2.val:
            current = list1
            buffer = list2
        else:
            current = list2
            buffer = list1

        head = current
        
        while current.next:
            if current.next.val >= buffer.val:
                temp = current.next
                current.next = buffer
                buffer = temp

            current = current.next

        current.next = buffer
            
        return head