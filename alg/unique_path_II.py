class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def dfs(obstacleGrid, m, n):

            ### out is right??? can read a number in the list by negative index.
            if m < 0 or n < 0:
                return 0
            ###
            if table[m][n] == -1:
                if m == 0 and n == 0:
                    return table[0][0]
                if obstacleGrid[m][n] == 1:
                    return 0
                table[m][n] = dfs(obstacleGrid, m - 1, n) + dfs(obstacleGrid, m, n - 1)
            return table[m][n]

        def dfs1(obstacleGrid, m, n):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return table[0][0]
            if obstacleGrid[m][n] == 1:
                return 0

            if table[m][n] != -1:
                return table[m][n]
            else:
                table[m][n] = dfs(obstacleGrid, m - 1, n) + dfs(obstacleGrid, m, n - 1)
                return table[m][n]

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        table = [[-1] * col for _ in range(row)]

        if obstacleGrid[0][0] == 0:
            table[0][0] = 1
        else:
            table[0][0] = 0

        return dfs(obstacleGrid, row - 1, col - 1)


a = Solution()
print(a.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
