class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        path = [-1 for _ in range(n)]
        print(path)
        res = []
        row = 0
        self.dfs(n, path, row, res)
        return res

    def dfs(self, n, path, row, res):
        if row == len(path):
            s = []
            for i in range(len(path)):
                r = ''
                for j in range(n):
                    if j == path[i]:
                        r += 'Q'
                    else:
                        r += '.'
                s.append(r)
            res.append(s)
            return

        for i in range(n):
            if self.is_valid(path, row, i):
                path[row] = i
                self.dfs(n, path, row + 1, res)

    def is_valid(self, path, row, col):
        for i in range(row):
            if path[i] == col:
                return False
            if abs(i - row) == abs(path[i] - col):
                return False
        return True


a = Solution()
print(a.solveNQueens(4))
