""" 70. Climbing Stairs
    Author: Artur Gasparyan
    Day: 18 Jan 2023
    Link: https://leetcode.com/problems/climbing-stairs/submissions/880435734/
"""


def climb_stairs(n, mem):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if n in mem:
        return mem[n]

    n_ways = climb_stairs(n-2, mem) + climb_stairs(n-1, mem)
    mem[n] = n_ways

    return n_ways 
            
        

class Solution:
    def climbStairs(self, n: int) -> int:
        return climb_stairs(n, {})