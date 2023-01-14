""" 242. Valid Anagram
    Author: Artur Gasparyan
    Date: 14 Jan 2023
    Link: https://leetcode.com/problems/valid-anagram/submissions/877951861/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base_ord = ord('a')
        char_count = [0 for _ in range(ord('z') - ord('a') + 1)]
        
        for c in s:
            char_count[ord(c) - base_ord] += 1

        for c in t:
            char_count[ord(c) - base_ord] -= 1

        return not any(char_count)