from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-anagrams-in-a-string/
    in real life, wouldn't update d_s, will create new one as the window slides for better readability;
    but to make it time O(n), need to update the counter hash map while slides

    this problem, window size is fixed.

    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        left, right = 0, len(p) - 1
        d_p = {}
        d_s = {}
        res = []

        for c in p:
            d_p[c] = d_p.get(c, 0) + 1
        for c in s[:len(p)]:
            d_s[c] = d_s.get(c, 0) + 1

        while right < len(s):
            if d_p == d_s:
                res.append(left)
            d_s[s[left]] -= 1
            if d_s[s[left]] == 0:
                del d_s[s[left]]
            left += 1
            right += 1

            if right < len(s):
                d_s[s[right]] = d_s.get(s[right], 0) + 1
        return res
