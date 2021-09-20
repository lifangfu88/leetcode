# 20 mins
# start from rotting ones, BFS, update distance, return the max(res)

import sys
from collections import deque
from typing import List

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    """
    https://leetcode.com/problems/rotting-oranges/
    start from rotten, BFS to update the min distance to rotten
    return the max of min distances of all the fresh
    if there is no fresh at all, return 0
    if there is un-reachable fresh, return -1

    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]

        stack = deque()
        fresh_exist = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    # start from all the rotten
                    stack.append((i, j))
                    res[i][j] = 0
                elif grid[i][j] == 0:
                    res[i][j] = -1
                elif grid[i][j] == 1:
                    fresh_exist = True
        # input doesn't contain fresh,
        if not fresh_exist:
            return 0

        # BFS to update the res to its closest rotten
        while stack:
            i, j = stack.popleft()
            for dx, dy in DIR:
                x, y = i + dx, j + dy
                if not (-1 < x < len(grid) and -1 < y < len(grid[0])):
                    continue

                if grid[x][y] == 1 and res[x][y] > res[i][j] + 1:
                    res[x][y] = res[i][j] + 1
                    stack.append((x, y))

        # return the max value of min distance to any rotten
        max_min = -1

        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] >= 0:
                    max_min = max(max_min, res[i][j])
        if max_min == sys.maxsize:
            max_min = -1
        return max_min
