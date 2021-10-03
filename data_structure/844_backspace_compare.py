from collections import deque


class Solution:
    """
    using stack to mimic the delete action
    O(n)
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        stack_s = deque()
        stack_t = deque()

        for c in s:
            if c != '#':
                stack_s.append(c)
            elif stack_s:
                stack_s.pop()

        for c in t:
            if c != '#':
                stack_t.append(c)
            elif stack_t:
                stack_t.pop()

        return stack_s == stack_t
