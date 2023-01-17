""" 278. First Bad Version
    Author: Artur Gasparyan
    Day: 17 Jan 2023
    Link: https://leetcode.com/problems/first-bad-version/submissions/879908361/
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi:
            mi = (lo + hi)//2

            if isBadVersion(mi):
                if not isBadVersion(mi-1):
                    return mi

                hi = mi - 1
            else:
                lo = mi + 1

        return mi+1