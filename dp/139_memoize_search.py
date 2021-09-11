from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cands = set()
        lens = set()
        for word in wordDict:
            if word in s:
                cands.add(word)
                lens.add(len(word))
        return self.dfs(s, lens, cands, {})

    def dfs(self, s:str, lens, cands, memo):
        if not s or s is '' or s in cands:
            return True

        if s in memo and memo[s]:
            return True
        if s in memo and not memo[s]:
            return

        for l in lens:
            if len(s) >= l:
                sub_s = s[:l]
                # print(sub_s, s[l:])
                if sub_s in cands:
                    left = s[l:]
                    res = self.dfs(left, lens, cands, memo)
                    if res:
                        memo[left] = True
                        return res
                    memo[left] = False


class SolutionBruteForce:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cands = set()
        lens = set()
        for word in wordDict:
            if word in s:
                cands.add(word)
                lens.add(len(word))
        return self.dfs(s, lens, cands)

    def dfs(self, s:str, lens, cands):
        if not s or s is '' or s in cands:
            return True

        for l in lens:
            if len(s) >= l:
                sub_s = s[:l]
                if sub_s in cands:
                    left = s[l:]
                    res = self.dfs(left, lens, cands)
                    if res:
                        return res
