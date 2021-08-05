
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        the min element meets:
        1. right element is larger than it;
        2. left element is larger than it.

        if no element meets this, return nums[0]
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        # 单调递增
        if nums[0] < nums[-1]:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # make sure nums[end] < nums[start]
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        # start + 1 == end
        return min(nums[start], nums[end])

