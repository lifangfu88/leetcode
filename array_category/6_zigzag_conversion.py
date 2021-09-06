class Solution:
    """
    key is to observe the index of value.
    1. when index modulo of numRows < numRows, put into dis[modulo]
    2. otherwise, put into dis[modulo + 2 - r],
    noticing that python supports negative index, so, r - m - 2 is easier to understand
    """

    def convert(self, s: str, numRows: int) -> str:

        res = ''
        if not s or not s:
            return None

        if len(s) <= numRows or numRows == 1:
            return s

        r = numRows
        dis = [[] for _ in range(r)]

        for i in range(len(s)):
            x = i % (2*r - 2)
            if x < r:
                dis[x].append(s[i])
            else:
                dis[r - x - 2].append(s[i])

        for i in range(len(dis)):
            res += ''.join(dis[i])

        return res
