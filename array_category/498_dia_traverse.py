from collections import defaultdict
from typing import List
# https://leetcode.com/problems/diagonal-traverse/


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])
        dia_sum = defaultdict(list)

        for i in range(m):
            for j in range(n):
                if (i + j) % 2:
                    dia_sum[i+j].append(mat[i][j])
                else:
                    dia_sum[i+j].insert(0, mat[i][j])

        res = []
        for i in range(m + n - 1):
            res += dia_sum[i]

        return res
