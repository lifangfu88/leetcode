class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        derived from # 1143
        https://leetcode-cn.com/problems/shortest-common-supersequence/solution/pythonzui-kuai-jie-fa-by-zhengchenarc/

        """
        m, n = len(str1), len(str2)

        dp = [['']  * (n + 1) for _ in range(m + 1)]
        # find the longest common subsequence
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]

        # build the shortestCommonSupersequence by adding chars not in LCS
        lcs = dp[m][n]
        i = j = 0
        ans = ''
        for c in lcs:
            while i < m and str1[i] != c:
                ans += str1[i]
                i += 1
            while j < n and str2[j] != c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        ans += str1[i:]
        ans += str2[j:]
        return ans
