from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 2D array, 2 status of up to the ith house
        dp = defaultdict(list)
        # init, first house, 0th means result of don't rob, 1th means rob
        dp[0] = [0, nums[0]]

        for i in range(1, len(nums)):
            dp[i] = [0, 0]
            # not robbing dp[i], i - 1 can be from 2 status
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

            # robbing dp[i], i - 1 is NOT robbed
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[len(nums) - 1])
