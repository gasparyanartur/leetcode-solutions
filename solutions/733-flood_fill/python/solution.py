""" 733. Flood Fill
    Author: Artur Gasparyan
    Date: 16 Jan 2023
    Link: https://leetcode.com/problems/flood-fill/submissions/879164476/
"""


offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        visited = set()
        frontier = [(sr, sc)]
        
        while frontier:
            coord = r, c = frontier.pop()
            if coord in visited:
                continue

            visited.add(coord)
            for dr, dc in offsets:
                n_coord = nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n and image[nr][nc] == start_color):
                    continue

                frontier.append(n_coord)

            image[r][c] = color

        return image 