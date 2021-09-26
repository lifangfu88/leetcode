from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return 0

        start, end = 0, len(nums) -1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # slope going up, set mid to start
            if nums[mid + 1] > nums[mid] > nums[mid - 1]:
                start = mid
            # slope going down, set mid to end
            else:
                end = mid
        if 0 < start < len(nums) - 1 and nums[start - 1] < nums[start] > nums[start + 1]:
            return start
        if start == 0 and nums[start] > nums[end]:
            return start

        if 0 < end < len(nums) - 1 and nums[end - 1] < nums[end] > nums[end + 1]:
            return end
        if end == len(nums) - 1  and nums[start] < nums[end]:
            return end

        return None
