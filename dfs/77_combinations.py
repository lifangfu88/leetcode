from typing import List
import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if not n or not k:
            return []

        cand = [i for i in range(1, n + 1)]

        res = []
        path = []
        visited = set()
        self.dfs(cand, 0, res, path, visited, k)

        return res

    def dfs(self, cand, pos, res, path, visited, tar):

        if len(path) == tar:
            res.append(copy.deepcopy(path))
            return

        if len(path) > tar or pos > len(cand):
            return

        # pruning
        if len(path) + len(cand) - pos < tar:
            return

        for i in range(pos, len(cand)):
            if cand[i] not in visited:
                visited.add(cand[i])
                self.dfs(cand, i, res, path + [cand[i]], visited, tar)
                visited.remove(cand[i])
