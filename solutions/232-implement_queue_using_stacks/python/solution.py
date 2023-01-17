""" 232. Implement Queue using Stacks
    Author: Artur Gasparyan
    Date: 17 Jan 2023
    Link: https://leetcode.com/problems/implement-queue-using-stacks/submissions/879895136/
"""


class MyQueue:

    def __init__(self):
        self.buffer, self.queue = [], []
        
    def push(self, x: int) -> None:
        self.buffer.append(x)

    def pop(self) -> int:
        if len(self.queue) == 0:
            while len(self.buffer) > 0:
                self.queue.append(self.buffer.pop())

        return self.queue.pop()

    def peek(self) -> int:
        if len(self.queue) == 0:
            while len(self.buffer) > 0:
                self.queue.append(self.buffer.pop())

        return self.queue[-1]


    def empty(self) -> bool:
        return len(self.queue) == 0 and len(self.buffer) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()