from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return []

        w_to_count = {}
        # O(n) word by count
        for w in words:
            if w not in w_to_count:
                w_to_count[w] = 1
            else:
                w_to_count[w] += 1

        # k * log(k)
        top_k_count = sorted(list(set(w_to_count.values())))[::-1]

        # count by word list
        count_to_ws = {}
        for w in w_to_count:
            count = w_to_count[w]
            if count not in count_to_ws:
                count_to_ws[count] = [w]
            else:
                count_to_ws[count].append(w)

        top_words = []

        # k * x * log(x)
        for count in top_k_count:
            top_words += sorted(count_to_ws[count])

        return top_words[:k]
