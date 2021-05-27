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

    val:   3, 4, -1, 2, 3
    index: 0, 1,  2, 3, 4

    #1:   3, 4,  3, 2, 3
    #2:   -1, 2,  3, 4, 3
    #3:   -1, 2,  3, 4, 3
    #4:   -1, 2,  3, 4, 3
    #5:   -1, 2,  3, 4, 3

    """
    n = len(nums)
    for i in range(n):
        val = nums[i]
        # only keep val that is in [1, n]
        while 1 <= val <= n and nums[val - 1] != val:
            # assign val to correct index
            nums[val - 1], val = val, nums[val - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

if __name__ == '__main__':
    print(first_missing([3, 4, 1, 8, 2, 2, 3]))


