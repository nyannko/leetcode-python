class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        f, l = 0, len(A) - 1
        while f <= l:
            if A[f] & 1 == 1 and A[l] & 1 == 0:
                A[f], A[l] = A[l], A[f]
                f += 1
                l -= 1
            if A[f] & 1 == 0:
                f += 1
            if A[l] & 1 == 1:
                l -= 1
        return A
