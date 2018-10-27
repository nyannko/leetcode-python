class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, "z")
                    count += 1
        return count

    def dfs(self, grid, i, j, s):
        print(grid[i][j], i, j, s)
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) \
                or grid[i][j] != '1':
            # print(grid[i][j], i, j, s)
            return

        grid[i][j] = '#'
        self.dfs(grid, i + 1, j, "a")
        self.dfs(grid, i - 1, j, "b")
        self.dfs(grid, i, j + 1, "c")
        self.dfs(grid, i, j - 1, "d")

a = Solution()
a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])