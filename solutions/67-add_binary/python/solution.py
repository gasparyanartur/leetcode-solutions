""" 67. Add Binary
    Author: Artur Gasparyan
    Date: 21 Jan 2023
    Link: https://leetcode.com/problems/add-binary/submissions/882358331/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"

        