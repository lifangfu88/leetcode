from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

        :param favoriteCompanies:
        :return:
        """
        i_to_f = {}
        for i in range(len(favoriteCompanies)):
            i_to_f[i] = set(favoriteCompanies[i])
        sub = set()
        for i in i_to_f.keys():
            for j in i_to_f.keys():
                if i != j and i_to_f[i].issubset(i_to_f[j]):
                    sub.add(i)
                    break
        res = []
        for i in range(len(favoriteCompanies)):
            if i not in sub:
                res.append(i)

        return res
