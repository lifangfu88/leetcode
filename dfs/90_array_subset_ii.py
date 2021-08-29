from typing import List
import copy


class Solution:
    """
    the only difference from subset I is de-dupe
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        self.dfs(sorted(nums), 0, res, path)

        return res

    def dfs(self, nums, pos, res, path):
        if path not in res:
            res.append(copy.deepcopy(path))

        for i in range(pos, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])
