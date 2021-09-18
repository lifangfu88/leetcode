from collections import deque
from typing import List


dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    """
    standard BFS, time: O(R*C), aka O(n), visit very value once
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not grid[i][j] or (i, j) in visited:
                    # only bfs when value is 1 AND not visited
                    continue
                res = max(res, self.bfs(grid, i, j, visited))
        return res

    def bfs(self, grid, x, y, visited):
        """
        return island size
        """
        visited.add((x, y))
        stack = deque([(x, y)])
        size = 0
        while stack:
            x, y = stack.popleft()
            size += 1
            grid[x][y] = -1
            for dx, dy in dir:
                x1, y1 = x + dx, y + dy
                if (x1, y1) in visited:
                    continue
                if -1 < x1 < len(grid) and -1 < y1 < len(grid[x1]):
                    if not grid[x1][y1] == 1:
                        continue

                    visited.add((x1, y1))
                    stack.append((x1, y1))

        return size
