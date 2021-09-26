from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        rotate 4 by definition
        """
        n = len(matrix)
        # why n/2, n/2? cause we rotate 4 values each time, only need to cover
        # 1/4 of the array to complete the rotation
        for i in range(n // 2):
            for j in range( (n + 1) // 2):
            # rotate the 4 val clock wise:
            # [i][j ]    ->  [j][n - 1 - i]
            #   /\                  \/
            # [n - j - 1][i] <- [n - 1 - i][n - 1 - j]
                start = matrix[i][j]

                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = start

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        mirror by diagonal, take reverse at each row
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
