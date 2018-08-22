class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # build a table
        row = len(grid)
        col = len(grid[0])

        table = [[0 for _ in range(col)] for _ in range(row)]

        table[0][0] = grid[0][0]
        for i in range(col):
            if i < 1: continue
            table[0][i] = table[0][i - 1] + grid[0][i]
        print(table)
        for i in range(row):
            if i < 1: continue
            table[i][0] = table[i - 1][0] + grid[i][0]
        print(table)
        for i in range(row):
            if i < 1: continue
            for j in range(col):
                if j < 1: continue
                table[i][j] = min(table[i - 1][j], table[i][j - 1]) + grid[i][j]
                print(grid[1][1])
        print(table)
        return table[row - 1][col - 1]


a = Solution()
print(a.minPathSum([[1,2],[1,1]]))  # 7
