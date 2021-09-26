class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        2重 2 pointers, 异向双指针
        O(n)
        brute force O(n^2)

        """
        if len(s) < 3:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                remove_r = s[l: r]
                if self.is_pali(remove_r):
                    return True
                remove_l = s[l + 1: r + 1]
                if self.is_pali(remove_l):
                    return True
                return False

        if l == r or s[l] == s[r]:
            return True
        return False

    def is_pali(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l < r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        return True
    # ========================================= #

    def validPalindrome_brute_force(self, s: str) -> bool:
        if not s or self.is_pali(s):
            return True

        for i in range(len(s) - 1):
            sub = s[:i] + s[i + 1:]
            if self.is_pali(sub):
                return True
        if self.is_pali(s[:len(s) - 1]):
            return True

        return False


    def is_pali(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l < r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        return True
