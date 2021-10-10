import sys
from collections import defaultdict
from typing import List


class WordDistance:
    """
    https://leetcode.com/problems/shortest-word-distance-ii/
    2 pointer, which pointer to +1? smaller one

    """

    def __init__(self, wordsDict: List[str]):
        self.loc = defaultdict(list)
        for i in range(len(wordsDict)):
            self.loc[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.loc[word1]
        loc2 = self.loc[word2]

        if not loc1 or not loc2:
            return -1
        res = sys.maxsize

        l, r = 0, 0

        while r < len(loc2) and l < len(loc1):
            res = min(res, abs(loc1[l] - loc2[r]))
            if loc1[l] > loc2[r]:
                r += 1
            else:
                l += 1
        return res





# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
