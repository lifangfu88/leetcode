from collections import defaultdict
import sys
from typing import List


class Solution:
    """
    the key is which point to move, as index is sorted, large one means smaller distance
    O(n)

    """
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        loc = defaultdict(list)

        for i, w in enumerate(wordsDict):
            if w == word1:
                loc[w].append(i)
            if w == word2:
                loc[w].append(i)

        p1, p2 = 0, 0
        res = sys.maxsize
        while p1 < len(loc[word1]) and p2 < len(loc[word2]):
            res = min(res, abs(loc[word1][p1] - loc[word2][p2]))
            if loc[word1][p1] < loc[word2][p2]:
                p1 += 1
            else:
                p2 += 1

        return res
