from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.helper(len(nums) - 1, nums, {})

    def helper(self, pos, nums, memo):
        if pos == 0:
            memo[0] = nums[0]
            return nums[0]

        if pos == 1:
            memo[1] = max(nums[0], nums[1])
            return memo[1]

        if pos in memo:
            return memo[pos]

        if pos - 1 in memo:
            a = memo[pos - 1]
        else:
            memo[pos - 1] = self.helper(pos - 1, nums, memo)
            a = memo[pos - 1]

        if pos - 2 in memo:
            b = memo[pos - 2]
        else:
            memo[pos - 2] = self.helper(pos - 2, nums, memo)
            b = memo[pos - 2]

        memo[pos] = max(memo[pos - 1], memo[pos - 2] + nums[pos])

        return memo[pos]
