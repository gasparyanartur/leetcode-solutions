""" Problem 36. Valid Sudoku
    Author: Artur Gasparyan
    Date: 21 Jan 2023
    Link: https://leetcode.com/problems/valid-sudoku/submissions/1027619675/
"""


class Solution:
    @staticmethod
    def isValidSudoku(board):
        rows = {chr(c): set() for c in range(49, 58)}
        cols = {chr(c): set() for c in range(49, 58)}
        subs = {chr(c): set() for c in range(49, 58)}

        for base_r in range(0, 9, 3):
            for base_c in range(0, 9, 3):
                for r in range(base_r, base_r + 3):
                    for c in range(base_c, base_c + 3):
                        cell = board[r][c]

                        if cell == ".":
                            continue

                        base = 3 * base_r + base_c
                        if (
                            (r in rows[cell])
                            or (c in cols[cell])
                            or (base in subs[cell])
                        ):
                            return False

                        rows[cell].add(r)
                        cols[cell].add(c)
                        subs[cell].add(base)

        return True
