from typing import List

L = [1, 2, 3]


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        path = ''
        self.dfs(s, 0, path, res)

        return res

    def dfs(self, s, pos, path, res):
        if pos > len(s) or path.count('.') > 3:
            return

        if len(path) == len(s) + 3:
            res.append(path)
            return

        for i in L:
            if pos + i <= len(s):
                seg = s[pos: pos + i]
                # eliminate leading 0
                if int(seg) != 0 and seg[0] == '0':
                    continue
                if int(seg) == 0 and len(seg) > 1:
                    continue

                if -1 < int(seg) < 256:
                    if path:
                        self.dfs(s, pos + i, path + '.' + seg, res)
                    else:
                        self.dfs(s, pos + i, seg, res)
