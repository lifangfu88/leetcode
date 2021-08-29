from typing import List
import copy
DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        self.dfs(sorted(candidates), target, path, res)

        return res

    def dfs(self, cans, tar, path, res):
        """
        when to exit the recursion
        when to dive into next level recursion

        """

        sup = sum(path)

        if sup > tar:
            return

        for i, val in enumerate(cans):
            # exit condition
            if val + sup == tar:
                path.append(val)
                sp = sorted(path)
                if sp not in res:
                    res.append(copy.deepcopy(sp))
            # goes beyond target, no need to add more
            elif val + sup > tar:
                return
            # has room to add more val
            elif val + sup < tar:
                self.dfs(cans, tar, path + [val], res)
