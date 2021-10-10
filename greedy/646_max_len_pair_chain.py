from typing import List

class Solution:
    """
    https://leetcode.com/problems/maximum-length-of-pair-chain
    when and why greedy works?
    greedy VS DP

    greedy has to be 'continuous linear' on best solution dimension
    """
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        pos = -1001
        res = 0
        for p in pairs:
            if p[0] > pos:
                res += 1
                pos = p[1]
        return res
