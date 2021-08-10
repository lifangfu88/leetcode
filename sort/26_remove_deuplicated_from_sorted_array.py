from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        112456667
        find the non-duplicate element and move them backwards.
        pointer res points to the updated non-duplicate index

        :param nums:
        :return:
        """

        if not nums:
            return 0

        res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                res += 1
                nums[res] = nums[i]

        return res + 1


if __name__ == '__main__':
    print(123)
