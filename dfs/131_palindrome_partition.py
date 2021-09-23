import copy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if len(s) == 1:
            return [[s]]

        res = []

        path = []

        self.dfs(0, path, res, s)

        return res

    def dfs(self, pos, path, res, s):

        if pos > len(s):
            return

        if len(path) > 0 and not self.is_pali(path[-1]):
            return

        if pos == len(s):
            if self.is_pali(path[-1]):
                res.append(copy.deepcopy(path))
            return

        for i in range(pos, len(s)):
            self.dfs(i + 1, path + [s[pos: i + 1]], res, s)

    def is_pali(self, s):
        return s == s[::-1]
