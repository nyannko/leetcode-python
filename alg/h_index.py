class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        N = len(citations)
        for i in range(N):
            # print i, citations[i], N - i
            if citations[i] >= N - i:
                return N - i
        return 0
