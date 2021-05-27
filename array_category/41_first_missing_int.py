from typing import List


def first_missing(nums: List[int]):
    """
    start point:
    1. mathematically, if one of the element > len(nums) or < 1;
        then the missing positive integer is in [1, len(nums) + 1]
    2. we can use hash set, loop twice to find the missing one;
    3. to make O(1) space, need to utilize the list index as hash key,
    put the element in the correct position
    utilize the index
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1



