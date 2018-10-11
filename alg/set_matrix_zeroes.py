class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        # use two bool list to record occurrence of zeroes
        rows = [0 for _ in range(row)]
        cols = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        # fill in with zeroes
        for i in range(row):
            if rows[i]:
                matrix[i] = [0 for _ in range(col)]
        for j in range(col):
            if cols[j]:
                for i in range(row):
                    matrix[i][j] = 0
