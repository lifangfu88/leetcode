"""
LC #80 Remove Duplicates from Sorted Array II

"""
from typing import List


def remove_duplicates(self, nums: List[int]) -> int:
    """
    1. sorted array;
    2. de-dupe problem with O(1) space means move element from right to left
    """
    if len(nums) < 3:
        return len(nums)

    left = 2
    for right in range(2, len(nums)):
        if nums[left - 2] != nums[right]:
            nums[left] = nums[right]
            left += 1

    return left
