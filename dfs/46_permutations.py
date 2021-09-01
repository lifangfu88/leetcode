from typing import List


class Solution:
    """
    recursion exit condition is different from the subset problems

    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, pos, res, path):
        n = len(nums)
        if len(path) == n:
            res.append(path)
            return

        for i in range(n):
            if nums[i] not in path:
                self.dfs(nums, i + 1, res, path + [nums[i]])
