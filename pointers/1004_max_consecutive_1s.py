class Solution:
    """
    O(n) solution, 2 pointers
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        # -> return the length of list which can contain at most k 0s
        l, r = 0, 0
        for r in range(len(nums)):
            # reduce k by 1
            if nums[r] == 0:
                k -= 1
            # illegal, increase left by one
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
