"""
Problem description:
http://lkw222.pythonanywhere.com/question_detail/search-in-a-sorted-array-of-unknown-size/
https://www.jiuzhang.com/solution/search-in-a-sorted-array-of-unknown-size/

the size of the array is actually bounded by these conditions:

1. You may assume that all elements in the array are unique.
2. The value of each element in the array will be in the range [-9999, 9999].

so, we can use binary search to reduce the size of the problem at each evaluation, we will need to:
1. start = 0, end = sys.maxsize, aka, the complete boundary of the array;
2. search in the array

both 2 steps can use binary search


This brings up another problem: what if the array is infinite?

in this case, we can use exponential expand to enlarge the range of search if target is larger than end:

1. set start to be pointing to 1st element and end pointing to 2nd element of array,
Now compare key with high index element:
2. if target is greater than end index element then copy end index in start index and double the end index.
3. if target is smaller, then apply binary search on start and end indices found.

"""
import sys

from typing import List


def mock_array_get(index):
    nums = [-1,0,3,5,9,12]
    return 2147483647 if index > len(nums) - 1 or index < 0 else nums[index]

def solution():
    start = 0
    end = sys.maxsize
    target = 2
    while start + 1 < end:
        # int size in Python 3 is not bounded
        mid = (start + end) // 2

        if mock_array_get(mid) == target:
            return mid
        elif mock_array_get(mid) > target:
            end = mid
        elif mock_array_get(mid) < target:
            start = mid

    if mock_array_get(start) == target:
        return start
    if mock_array_get(end) == target:
        return end

    return -1


def infinite_sorted_array(nums: List, target: int):
    """
    solution for infinite array

    :param nums:
    :param target:
    :return:
    """
    start = 0
    end = 1
    while start + 1 < end:
        if nums[end] < target:
            end = 2 * end
            continue
        # at this place: nums[end] >= target
        # aka, the upper boundary of array is found
        # start binary search
        mid = (start + end) // 2
        if nums(mid) < target:
            start = mid
        elif nums(mid) > target:
            end = mid
        else:
            return mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end

    return -1














