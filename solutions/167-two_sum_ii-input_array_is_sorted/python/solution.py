""" Problem 167. Two Sum II - Input Array is Sorted
    Author: Artur Gasparyan
    Date: 21 Jan 2023
    Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1027623650/
"""


class Solution:
    @staticmethod
    def twoSum(numbers, target):
        i = 0
        j = len(numbers) - 1
        while True:
            s = numbers[i] + numbers[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [i + 1, j + 1]
