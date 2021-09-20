from typing import List
import copy


class Solution:
    """
    O(4^n), as there are 4 options at most at one position

    """

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

        if not digits:
            return []

        res = set()

        self.dfs(mapping, digits, 0, res, '')

        return list(res)

    def dfs(self, mapping, dig, pos, res, path):

        if len(path) > len(dig):
            return
        if len(path) == len(dig) and path not in res:
            res.add(copy.deepcopy(path))
            return

        for j in mapping[dig[pos]]:
            self.dfs(mapping, dig, pos + 1, res, path + j)
