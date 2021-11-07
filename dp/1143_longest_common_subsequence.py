class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/
        dp[i][j]:
            dp[i][j]表示 text1[0:i-1] 和 text2[0:j-1]的最长公共子序列。
            （注：text1[0:i-1] 表示的是 text1 的 第 0 个元素到第 i - 1 个元素，两端都包含）

        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
