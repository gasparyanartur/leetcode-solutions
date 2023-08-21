""" Problem 150. Evaluate Reverse Polish Notation
    Author: Artur Gasparyan
    Date: 21 Aug 2023
    Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1027627731/
"""


import math


class Solution:
    @staticmethod
    def evalRPN(tokens):
        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                q = a / b
                q = math.ceil(q) if q < 0 else math.floor(q)
                stack.append(q)
            else:
                stack.append(int(token))

        return stack[0]
