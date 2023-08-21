""" Problem 739. Daily Temperatures
    Author: Artur Gasparyan
    Date: 21 Aug 2023
    Link: https://leetcode.com/problems/daily-temperatures/submissions/1026622383/
"""


import array


class Solution:
    @staticmethod
    def dailyTemperatures(temperatures):
        # Iterate over the temperatures
        # Maintain a stack
        temps = array.array("I", [0 for _ in temperatures])
        i_stack = []
        t_stack = []

        for i, t in enumerate(temperatures):
            while t_stack and t > t_stack[-1]:
                i_stored = i_stack.pop()
                temps[i_stored] = i - i_stored
                t_stack.pop()

            i_stack.append(i)
            t_stack.append(t)

        return temps
