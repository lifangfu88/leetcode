from typing import List
import copy


class Solution:
    """
    back tracking,
    same to the permutation, starting index can be [0, len(nums) - 1],
    dfs from each starting index
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(sorted(nums), 0, res, path)

        return res

    def dfs(self, nums, pos, res, path):
        res.append(copy.deepcopy(path))

        for i in range(pos, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])
