from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        similar to #153
        difference is in exist condition:

        153:
         /
        /
            /
           /

        154: there are flat situation

           /
        __/
               __
            __/

        then the key is to eliminate the flat case by making end -= 1
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            print(start, end)
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] <= nums[mid + 1]:
                return nums[mid]
            elif nums[start] == nums[end]:
                end -= 1
            elif nums[start] < nums[end]:
                return nums[start]

            # nums[start] > nums[end]
            else:
                if nums[mid] >= nums[start]:
                    start = mid
                else:
                    end = mid
        return min(nums[start], nums[end])
