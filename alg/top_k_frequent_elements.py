class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # same as topk frequent elements 60ms
        from collections import Counter
        elements = Counter(nums)
        res = sorted(elements.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in res][:k]

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter  # dict
        import heapq  # sort
        elements = Counter(nums)
        freq = []

        # push all the elements into a heap
        # python min heap
        for ele, count in elements.items():
            heapq.heappush(freq, (ele, count))
            # if len(freq) > k:
            #     heapq.heappop(freq)

        # get the top k frequent elements
        res = []
        for i in heapq.nlargest(k, freq, key=lambda x: x[1]):
            res.append(i[0])
        return res

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [k for k, v in Counter(nums).most_common(k)]

    def topKFrequent3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq

        elements = {}
        freq = []

        for i in nums:
            elements[i] = elements.get(i, 0) + 1
        # elements = Counter(nums)
        for num, count in elements.items():
            heapq.heappush(freq, (count, num))
            if len(freq) > k:
                heapq.heappop(freq)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])
        return res[::-1]
