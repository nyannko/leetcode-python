class Solution(object):
    def minimum_total(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i, row in reversed(list(enumerate(triangle[:-1]))):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
                # print(i, j, triangle[i][j])
        return triangle[0][0]
