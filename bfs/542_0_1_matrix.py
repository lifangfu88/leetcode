from collections import deque

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if not matrix or not matrix[0]:
            return []

        n, m = len(matrix), len(matrix[0])

        queue = []
        for i in range(n):
            for j in range(m):
                # 将所有的0当做起始点
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = n + m  # 曼哈顿距离在一个矩阵中的最大值（不严格，反正比最大值大就行）

        while queue:
            point = queue.pop(0)

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = dx + point[0]
                y = dy + point[1]

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                # 当前是洼地，更新周边距离
                if matrix[point[0]][point[1]] < matrix[x][y]:
                    matrix[x][y] = matrix[point[0]][point[1]] + 1
                    queue.append((x, y))
        return matrix

import sys
from collections import deque
from typing import List

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 7:00
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])

        res = [[sys.maxsize for _ in range(len(mat[0]))] for _ in range(len(mat))]

        stack = deque()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    stack.append((i, j))

        while stack:
            i, j = stack.popleft()

            for dx, dy in DIR:
                x, y = dx + i, dy + j
                if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]):
                    continue
                if res[i][j] < res[x][y]:
                    res[x][y] = res[i][j] + 1
                    stack.append((x, y))
        return res
