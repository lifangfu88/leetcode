"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

"""

class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0

        if len(s) < 2:
            return len(s)

        left, right = 0, 1
        cout_d = {}
        res = 0
        for i in range(left, right + 1):
            cout_d[s[i]] = cout_d.get(s[i], 0) + 1

        while right < len(s):
            print(left, right, cout_d)
            if len(cout_d.keys()) < 3:
                if right - left + 1 > res:
                    res = right - left + 1
            else:
                cout_d[s[left]] -= 1
                if cout_d[s[left]] == 0:
                    del cout_d[s[left]]
                left += 1
            right += 1
            if right < len(s):
                cout_d[s[right]] = cout_d.get(s[right], 0) + 1

        return res





