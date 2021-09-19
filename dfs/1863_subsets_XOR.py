from typing import List
import copy


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        path = []
        self.dfs(0, nums, path, subsets)

        res = 0
        for sub in subsets:
            res += self.xor(sub)

        return res

    def xor(self, sub):

        if len(sub) == 0:
            return 0

        if len(sub) == 1:
            return sub[0]

        res = sub[0]
        for i in range(1, len(sub)):
            res = res ^ sub[i]
        return res

    def dfs(self, pos, nums, path, subsets):
        subsets.append(copy.deepcopy(path))

        for i in range(pos, len(nums)):
            # i + 1 to move on to next element
            # path + [nums[i]] to append before recursion and pop after recursion
            self.dfs(i + 1, nums, path + [nums[i]], subsets)
