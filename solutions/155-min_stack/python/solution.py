""" Problem 155. Min Stack
    Author: Artur Gasparyan
    Date: 19 Aug 2023
    Link: https://leetcode.com/problems/min-stack/submissions/1025692834/
"""


import heapq


class MinStack:
    def __init__(self):
        self.count = {}
        self.heap = []
        self.stack = []

    def push(self, val: int) -> None:
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1

        heapq.heappush(self.heap, val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop(-1)

        if self.count[val] > 0:
            self.count[val] -= 1

        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.count[self.heap[0]] == 0:
            heapq.heappop(self.heap)

        return self.heap[0]
