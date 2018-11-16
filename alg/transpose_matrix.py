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

    def transpose2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[row[i] for row in A] for i in range(len(A[0]))]


a = Solution()
print(a.transpose2([[1, 2, 3], [4, 5, 6]]))
