from collections import defaultdict


class Solution:
    """
    同余：nums[i:j] 可整除 k means: nums[:j] and nums[:i] 同余

    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or not k:
            return False

        # 同余
        residual = defaultdict(list)
        pre_sum = 0
        for i, n in enumerate(nums):
            pre_sum += n
            resid = pre_sum % k
            # result sub array start from 0
            if not resid and i > 0:
                return True

            if resid in residual and i - residual[resid][0] > 1:
                return True

            residual[resid].append(i)

        return False
