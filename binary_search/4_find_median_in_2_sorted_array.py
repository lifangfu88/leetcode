from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1. median, move (len(A) + len(B)) //2 steps

        2 pointers, pointing to 2 list and start to move, move the smaller one

        """

        l1 = len(nums1)
        l2 = len(nums2)

        # pointers
        p1, p2 = 0, 0

        # value
        left, right = -1, -1

        for i in range((l1 + l2) // 2 + 1):
            left = right

            if p1 < l1 and nums1[p1] <= nums2[p2]:
                right = nums1[p1]
                p1 += 1
            else:
                right = nums2[p2]
                p2 += 1
        if (l1 + l2) % 2:
            return right
        return (left + right) / 2


    def findMedianSortedArrays_2(self, A: List[int], B: List[int]) -> float:

        m, n = len(A), len(B)
        if (m + n) % 2 == 1:
            return self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2  + 1)
        left = self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2)
        right = self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2 + 1)
        return (left + right) / 2

    def getKth(self, A, start1, end1, B, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if (len1 > len2):
            return self.getKth(B, start2, end2, A, start1, end1, k)
        if (len1 == 0):
            return B[start2 + k - 1]
        if k == 1:
            return min(A[start1], B[start2])
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if (A[i] > B[j]):
            return self.getKth(A, start1, end1, B, j + 1, end2, k - (j - start2 + 1))

        return self.getKth(A, i + 1, end1, B, start2, end2, k - (i - start1 + 1))
