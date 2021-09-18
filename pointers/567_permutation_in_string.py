class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        https://leetcode.com/problems/permutation-in-string/

        permutation match, means char counter matches
        using sliding window to solve it.


        :param s1:
        :param s2:
        :return:
        """
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1)
        s1_counter = self.counter(s1)

        while right <= len(s2):
            s2_sub_counter = self.counter(s2[left:right])
            if s1_counter == s2_sub_counter:
                return True
            left += 1
            right += 1

        return False

    def counter(self, s):
        res = {}
        for c in s:
            if not c in res:
                res[c] = 1
            else:
                res[c] += 1

        return res
