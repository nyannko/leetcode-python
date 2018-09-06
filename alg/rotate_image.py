class Solution:
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = [i[:] for i in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = len(matrix[0]) - 1 - i
                print(i, j, m)
                n[j][m] = matrix[i][j]
        return n

    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # In leetcode, use reverse instead of slice..
        matrix.reverse()
        # matrix = matrix[::-1]
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        for i in matrix:
            i.reverse()

        print(matrix)


a = Solution()
print(a.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
