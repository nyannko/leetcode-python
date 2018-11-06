class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        n = len(A)
        presum = [0 for i in range(n + 1)]
        res = 0
        total = 0

        for i in range(n):
            res += A[i]
            comp = res - S

            if comp >= 0:
                total += presum[comp]

            if res == S:
                total += 1
            presum[res] += 1
            # print res, comp, presum, total
        return total
