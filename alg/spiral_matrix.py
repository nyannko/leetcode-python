import math


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        row = len(matrix)
        col = len(matrix[0])
        nums = math.ceil(min(row / 2, col / 2))
        res = []
        print([x for x in range(nums)])
        for i in [x for x in range(nums)]:
            res.extend(self.cycle(matrix, row, col, i))
        return res

    def cycle(self, matrix, row, col, start):
        res = []

        s_i, s_j = start, start

        for i in range(s_i, col - s_j):
            res.append(matrix[s_i][i])

        for i in range(s_i + 1, row - s_i - 1):
            print(i, row, col)
            res.append(matrix[i][col - s_j - 1])

        if row - s_i - 1 > s_i:
            for i in reversed(range(s_i, col - s_j)):
                res.append(matrix[row - s_i - 1][i])

        if col - s_j - 1 > s_j:
            for i in reversed(range(s_i + 1, row - s_i - 1)):
                res.append(matrix[i][s_i])

        return res


a = Solution()
print(a.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))
print(a.spiralOrder([[1, 2, 3, 4, 5, 6, 7, 8, 9]]))
print(a.spiralOrder([[2, 5, 8], [4, 0, -1]]))
print(a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 1. diagonal line: starting point, division
# 2. boundary check
# 3. check if the same line
