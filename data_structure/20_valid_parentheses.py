from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        left = ['(', '[', '{']
        right = [')', ']', '}']

        stack = deque()

        if not s or s[0] in right or len(s) % 2:
            return False

        for c in s:
            if c in left:
                stack.append(c)
            else:
                i = right.index(c)
                if len(stack) < 1 or stack[-1] != left[i]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
