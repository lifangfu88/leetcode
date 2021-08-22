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
