
from collections import defaultdict


class Solution:
    """
    https://leetcode.com/problems/subarray-sum-equals-k/solution/
    the hashmap solution is interesting, leverage pre-sum as we only
    need the count/occurrence

    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)

        pre_sum = 0
        count = 0
        map[0] = 1
        for n in nums:
            pre_sum += n
            if pre_sum - k in map:
                count += map[pre_sum - k]
            map[pre_sum] += 1

        return count
