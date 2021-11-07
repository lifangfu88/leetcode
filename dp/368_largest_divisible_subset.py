class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # avoid unnecessary blocking
        # i.e. 1,2,8,4
        nums.sort()
        # max element in divisible subset
        max_n = copy.deepcopy(nums)
        # legit subset ending with i
        dp = [[n] for n in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % max_n[j]:
                    continue
                if len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    max_n[i] = max(max_n[i], max_n[j])
        leng = 1

        for l in dp:
            if len(l) >= leng:
                res = l
                leng = len(l)

        return res
