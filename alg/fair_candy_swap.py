class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in set(B):
            if diff + b in A:
                return [diff + b, b]
