from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag_dict = {}
        for s in strs:
            s_s = ''.join(sorted(s))
            if s_s in ag_dict:
                ag_dict[s_s].append(s)
            else:
                ag_dict[s_s] = [s]

        return [i for i in ag_dict.values()]
