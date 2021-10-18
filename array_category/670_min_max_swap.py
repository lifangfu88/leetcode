from collections import defaultdict


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        https://leetcode.com/problems/maximum-swap/
        """
        s_num = str(num)
        s_num_list = [c for c in s_num]
        num_list = [c for c in s_num]
        num_list.sort(reverse = True)

        if s_num == ''.join(num_list):
            return num

        v2i = defaultdict(list)

        for i, n in enumerate(s_num):
            v2i[n].append(i)

        for i, n in enumerate(s_num):
            if num_list[i] == n:
                continue
            fwd_i = v2i[num_list[i]][-1]
            bwd_i = i
            break

        s_num_list[fwd_i], s_num_list[bwd_i] = s_num_list[bwd_i], s_num_list[fwd_i]

        return int(''.join(s_num_list))
