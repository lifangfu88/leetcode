from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-duplicates-in-an-array/

    note that the description is:
    1. at most 2 times;
    2. value range is [1, n]

    solution: leverage the index to store the duplication

    Time: O(n)
    Space: O(1)

    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(i + 1)
            nums[abs(nums[i]) - 1] *= -1

        return [abs(nums[i -1]) for i in res]
