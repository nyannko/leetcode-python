class KthLargest(object):

    def __init__(self, k, nums):
        import heapq
        self._heap = nums
        heapq.heapify(self._heap)
        self.k = k
        while len(self._heap) > k:
            heapq.heappop(self._heap)

    def add(self, val):
        if len(self._heap) < self.k:
            heapq.heappush(self._heap, val)
        else:
            # replace the previous value on the heap
            heapq.heappushpop(self._heap, val)  # ?
        return self._heap[0]
