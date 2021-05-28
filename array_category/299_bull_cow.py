from collections import defaultdict


def getHint(self, secret: str, guess: str) -> str:
    """
    https://leetcode.com/problems/bulls-and-cows

    :param self:
    :param secret:
    :param guess:
    :return:
    """
    if not secret or not guess or not len(secret) == len(guess) :
        return '0A0B'

    n = len(secret)
    a, b = 0, 0
    # return 0 while key is missing.
    s = defaultdict(int)
    g = defaultdict(int)
    for i in range(n):
        if secret[i] == guess[i]:
            # loop thru, find A, matching count at same index
            a += 1
        else:
            # record num : count
            s[secret[i]] += 1
            g[guess[i]] += 1
    # loop thru again, find matching count at different index
    for k, v in s.items():
        b += min(s[k], g[k])

    return str(a) + 'A' + str(b) + 'B'
