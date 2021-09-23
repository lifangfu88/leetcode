from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        path = ''
        res = []
        self.dfs(0, path, res, s)

        return res

    def dfs(self, pos, path, res, s):
        if len(path) == len(s) and path not in res:
            res.append(path)
            return

        if len(path) > len(s):
            return

        for i in range(pos, len(s)):
            if s[i].isalpha():
                self.dfs(i + 1, path + s[i].lower(), res, s)
                self.dfs(i + 1, path + s[i].upper(), res, s)
            else:
                self.dfs(i + 1, path + s[i], res, s)
