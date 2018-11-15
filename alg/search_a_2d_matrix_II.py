class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        r, c = 0, len(matrix[0]) - 1

        while c >= 0 and r < len(matrix):
            if target == matrix[r][c]:
                return True
            if target < matrix[r][c]:
                c -= 1
            if target > matrix[r][c]:
                r += 1
        return False
