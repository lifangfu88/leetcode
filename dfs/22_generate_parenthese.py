from typing import List
"""
https://leetcode.com/problems/generate-parentheses/

time: O(2**n)
key: 1. add `(` then `)` to avoid invalid case, count of ( and ) will enforce the validation 
     2. definition of recursion
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        self.dfs(0, 0, '', res, n)

        return res

    def dfs(self, l_count, r_count, curr, res, n):
        if l_count < r_count:
            return
        if l_count > n or r_count > n:
            return

        if l_count == n and r_count == n:
            res.append(curr)
            return

        # add left first
        self.dfs(l_count + 1, r_count, curr + '(', res, n)

        self.dfs(l_count, r_count + 1, curr + ')', res, n)
