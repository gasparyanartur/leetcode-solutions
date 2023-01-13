""" Problem 125. Valid Palindrome
    Author: Artur Gasparyan
    Date: 13 Jan 2023
    Link: https://leetcode.com/problems/valid-palindrome/submissions/877394661/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            lcode = ord(s[i])
            rcode = ord(s[j])

            while i < j and not (      # Find next valid char from left
                65 <= lcode <= 90 or     # Upper case
                97 <= lcode <= 122 or    # Lower case
                48 <= lcode <= 57        # Digit
            ):     
                i += 1
                lcode = ord(s[i])

            while i < j and not (      # Find next valid char from right
                65 <= rcode <= 90 or     # Upper case
                97 <= rcode <= 122 or    # Lower case
                48 <= rcode <= 57        # Digit
            ):     
                j -= 1
                rcode = ord(s[j])

            if j <= i:                               # None found
                break

            if (s[i] != s[j]):      # They are different either means that it is not a palindrome, or that they have different casing
                if not (            # Check for casing
                    (65 <= lcode <= 90 and rcode == lcode + 32) or  # Left is upper and right is lower equivalent
                    (65 <= rcode <= 90 and lcode == rcode + 32)     # Right is upper and left is lower equivalent
                ):
                    return False

            i += 1
            j -= 1

        return True
