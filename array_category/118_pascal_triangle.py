from typing import List


def generate(num_rows: int) -> List[List[int]]:
    """
    https://leetcode.com/problems/pascals-triangle/

    :param num_rows:
    :return:
    """
    if num_rows < 1:
        return [[]]
    if num_rows == 1:
        return [[1]]

    res = [[1]]

    for _ in range(num_rows - 1):
        num = res[-1]
        new = [1] * (len(num) + 1)
        for i in range(1, len(num)):
            new[i] = num[i - 1] + num[i]

        res.append(new)

    return res
