""" 169. Majority Element
    Author: Artur Gasparyan
    Date: 20 Jan 2023
    Link: https://leetcode.com/problems/majority-element/description/
"""

import statistics

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(statistics.median(nums))

        