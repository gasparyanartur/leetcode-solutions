""" 383. Ransom Note
    Author: Artur Gasparyan
    Date: 17 Jan 2023
    Link: https://leetcode.com/problems/ransom-note/submissions/880138478/
"""


import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)

        return all((c in mag_count and n <= mag_count[c] for (c, n) in note_count.items()))