""" 776. Binary Search
    Author: Artur Gasparyan
    Date: 14 Jan 2024
    Link: https://leetcode.com/problems/binary-search/submissions/877955526/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mi = lo + (hi-lo)//2

            if nums[mi] < target:
                lo = mi+1

            elif nums[mi] > target:
                hi = mi-1

            else:
                return mi

        return -1