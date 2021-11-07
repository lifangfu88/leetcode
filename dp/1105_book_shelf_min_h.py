class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # min height of the previous i books
        dp = [sys.maxsize] * (len(books) + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            # assume i is the last book of last level
            # adjust books before i, check if lower height is acheivable
            level_w = 0
            level_h = 0
            for j in range(i, 0, -1):
                level_w += books[j-1][0]
                # cannot update any more
                if level_w > shelfWidth:
                    # all before j is optimized
                    break
                level_h = max(level_h, books[j-1][1])
                dp[i] = min(dp[i], dp[j - 1] + level_h)
                j -= 1
        return dp[-1]
