class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        row = len(matrix)    #4
        col = len(matrix[0]) #5
        H, L, R = [0]*col, [0]*col, [col]*col  #5

        res = 0
        for i in range(row):
            left = 0
            right = col
            for j in range(col):
                if matrix[i][j] == '1':
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j + 1
                    H[j]= L[j]= 0
                    R[j] = col

            for j in reversed(range(col)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    res = max(res, H[j] * (R[j] - L[j]))
                else:
                    right = j

        return res

a = Solution()
print(a.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))