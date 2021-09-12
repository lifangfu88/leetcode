class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1

        left, right = 0, 1
        res = 0

        while right < len(s) + 1:
            sub = s[left:right]
            if self.is_unique(sub):
                right += 1
                if right - left - 1 > res:
                    res = right -left - 1
            else:
                left += 1
                right += 1

        return res


    def is_unique(self, s):
        chars = [c for c in s]

        return len(chars) == len(set(chars))
