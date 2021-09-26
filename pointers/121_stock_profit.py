from typing import List
import sys



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        internal prices don't matter
        only need to make sure from left to right, update the min and max delta
        O(n)
        :param prices:
        :return:
        """
        if len(prices) == 1:
            return 0

        min_p = sys.maxsize

        res = 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            res = max(res, prices[i] - min_p)

        return res
