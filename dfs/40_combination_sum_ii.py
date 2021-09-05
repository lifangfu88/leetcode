from typing import List
import copy


class Solution:
    """
    https://leetcode.com/problems/combination-sum-ii


    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not target or not candidates or target > sum(candidates):
            return []

        path = []
        res = []
        self.dfs(sorted(candidates), target, 0, path, res)

        return res

    def dfs(self, nums, tar, pos, path, res):
        if sum(path) == tar and path not in res:
            res.append(copy.deepcopy(path))
            return

        if sum(path) > tar:
            return

        for i in range(pos, len(nums)):
            # attention on this condition to avoid excessive explore
            if nums[i] == nums[i-1] and i > pos:
                continue
            self.dfs(nums, tar, i + 1, path + [nums[i]], res)
