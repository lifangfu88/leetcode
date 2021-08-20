from typing import List
from collections import deque

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    BFS, need to memorize the visited island

    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """

        """
        if not grid or not grid[0]:
            return 0

        visited = set()
        ret = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # iterate, when find new "1", make it the start point of BFS
                if grid[i][j] is "1" and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    ret += 1

        return ret

    def bfs(self, i, j, grid, visited):
        """
        BFS the given array
        :param i:
        :param j:
        :param grid:
        :param visited:
        :return:
        """
        queue = deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            visited.add((x, y))
            for a, b in DIRECTIONS:

                if self.is_valid(len(grid), len(grid[0]), a + x, b + y) \
                        and grid[a + x][b + y] is "1" \
                        and (a + x, b + y) not in visited:
                    visited.add((a + x, b + y))
                    queue.append((a + x, b + y))

    def is_valid(self, a, b, i, j):
        """
        validate if the index is in bound
        :param a:
        :param b:
        :param i:
        :param j:
        :return:
        """
        return -1 < i < a and -1 < j < b
