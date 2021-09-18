from collections import deque
from typing import List

"""
https://leetcode.com/problems/flood-fill/
BFS / DFS, using memo to avoid repeat visit

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dir = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        visited = set()

        stack = deque([(sr, sc)])

        originalColor = image[sr][sc]

        while stack:
            x, y = stack.popleft()
            image[x][y] = newColor
            visited.add((x, y))
            for dx, dy in dir:
                x1 = x + dx
                y1 = y + dy
                if (x1, y1) in visited:
                    continue
                if -1 < x1 < len(image) and -1 < y1 < len(image[0]) and image[x1][y1] == originalColor:
                    stack.append((x1, y1))

        return image
