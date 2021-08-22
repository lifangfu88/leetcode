from collections import deque
from typing import List
"""https://www.jiuzhang.com/solution/word-ladder/"""


class Solution:
    """
    iterate 26 char in alphabet, just try
    tip: distance is level/depth of the BFS, not how many words you've tried
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        dist = 0
        que = deque([beginWord])
        visited = set(beginWord)
        while que:
            dist += 1
            for _ in range(len(que)):
                w = que.popleft()
                if w == endWord:
                    return dist
                for n_w in self.next_words(w):
                    if n_w in wordList and n_w not in visited:
                        que.append(n_w)
                        visited.add(n_w)

        return 0

    def next_words(self, word):

        words = set()

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for delta in 'abcdefghijklmnopqrstuvwxyz':
                words.add(left + delta + right)
        return words
