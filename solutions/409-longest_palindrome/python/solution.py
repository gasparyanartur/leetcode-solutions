""" 409. Longest Palindrome
    Author: Artur Gasparyan
    Date: 18 Jan 2023
    Link: https://leetcode.com/problems/longest-palindrome/submissions/880450183/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        
        n_pairs_all = 0
        n_unique = False

        for cnt in counter.values():
            n_pairs, n_unpaired = divmod(cnt, 2)
            
            n_unique += n_unpaired
            n_pairs_all += n_pairs

        return 2 * n_pairs_all + bool(n_unique)