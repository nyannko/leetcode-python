class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] \
                for j in range(len(A[0]))]

    def transpose1(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # zip usage
        return zip(*A)
