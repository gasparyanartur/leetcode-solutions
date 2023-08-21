""" Problem 20. Valid Parenthesis
    Author: Artur Gasparyan
    Date: 21 Jan 2023
    Link: https://leetcode.com/problems/valid-parentheses/submissions/1025677980/
"""


class Solution:
    @staticmethod
    def isValid(s):
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False

                m = stack.pop(-1)
                if (
                    (m == "(" and c != ")")
                    or (m == "[" and c != "]")
                    or (m == "{" and c != "}")
                ):
                    return False

        return not stack
