from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        decade into a basic house robbery #198 problem
        implies an idea to solve cyclic problem:
        break it into an acyclic problem

        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = defaultdict(list)
        dp[0] = [0, nums[0]]

        # 0 to n - 1
        for i in range(1, len(nums) - 1):
            dp[i] = [0, 0]

            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        # 1 to n
        dp2 = defaultdict(list)
        dp2[1] = [0, nums[1]]
        for i in range(2, len(nums)):
            dp2[i] = [0, 0]

            dp2[i][0] = max(dp2[i - 1])
            dp2[i][1] = dp2[i - 1][0] + nums[i]

        res = max(dp[len(nums) - 2] + dp2[len(nums) - 1])

        return res
