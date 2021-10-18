

class Solution:
    def calculate(self, s: str) -> int:
        """
        https://leetcode.com/problems/basic-calculator-ii/
        do the calculation after get the right operand
        using stack to delay the calculation
        """
        num = 0
        # last seen sign
        operator = '+'
        stack = []
        for i, c in enumerate(s):

            if c.isnumeric():
                num = num*10 + int(c)

            if (not c.isnumeric() and not c == ' ') or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    left = stack.pop()
                    stack.append(left * num)
                elif operator == '/':
                    left = stack.pop()
                    if left // num < 0 and left%num:
                        stack.append(left // num + 1)
                    else:
                        stack.append(left // num)

                operator = c
                num = 0
        return sum(stack)
