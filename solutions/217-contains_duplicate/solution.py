""" 217. Contains duplicate
    Author: Artur Gasparyan
    Date: 21 Aug 2023
    Link: https://leetcode.com/problems/contains-duplicate/submissions/1027589550/
"""


class Solution:
    @staticmethod
    def containsDuplicate(nums):
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
