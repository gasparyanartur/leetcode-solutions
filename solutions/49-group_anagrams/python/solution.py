""" 49. Group Anagrams
    Author: Artur Gasparyan
    Date: 21 Aug 2023
    Link: https://leetcode.com/problems/group-anagrams/submissions/1027614945/
"""


class Solution:
    @staticmethod
    def groupAnagrams(strs):
        groups = {}

        for s in strs:
            ss = hash(tuple(sorted(s)))
            if ss in groups:
                groups[ss].append(s)
            else:
                groups[ss] = [s]

        return groups.values()