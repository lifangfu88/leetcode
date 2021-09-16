import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Brute Force, double for loop, O(n^2)
        prefix_sum: O(n)

        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]

        pre_sum = [sum(nums[:i]) for i in range(1, len(nums) + 1)]
        # important, ignore positive min_prefix
        minp = 0
        maxp = -sys.maxsize
        for pre in pre_sum:
            maxp = max(maxp, pre - minp)
            minp = min(minp, pre)

        return maxp
