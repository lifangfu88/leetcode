import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-wrnt/
        """
        # at one day, there are 4 possibilities:
        # state instead of action
        # 1. hold 1st
        # 2. sold 1st
        # 3. hold 2nd
        # 4. sold 2nd

        if not prices or len(prices) < 2:
            return 0
        dp = []
        dp.append([-prices[0], 0, -prices[0], 0])
        for i in range(1, len(prices)):
            x = [0 for _ in range(4)]
            x[0] = max(dp[i - 1][0], -prices[i])
            x[1] = max(dp[i - 1][0] + prices[i], dp[i-1][1])
            x[2] = max(dp[i-1][1] - prices[i], dp[i-1][2])
            x[3] = max(dp[i-1][2] + prices[i], dp[i-1][3])
            dp.append(x)
        return max(dp[-1])
