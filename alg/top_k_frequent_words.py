import heapq
import functools


@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.word == other.word and self.count == other.count


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # from collections import Counter
        # words_list = Counter(words)
        # s = sorted(words_list.items(), key=lambda m:m[1], reverse=True)
        # print(s)
        # return [x[0] for x in s][:k]

        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1

        freq = []
        heapq.heapify(freq)
        for word, count in d.items():
            heapq.heappush(freq, (Element(count, word), word))
            if len(freq) > k:
                heapq.heappop(freq)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])
        return res[::-1]
