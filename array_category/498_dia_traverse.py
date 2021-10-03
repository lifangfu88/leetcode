from collections import defaultdict
from typing import List
# https://leetcode.com/problems/diagonal-traverse/


class Solution:
    """
    elements on the same dia meet this condition:
    i+j is the same
    thus, we can key on i+j for each element list
    plus, the order in each list is decided by odd/even of i+j

    O(n)
    """
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
