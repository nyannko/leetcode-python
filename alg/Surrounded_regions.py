class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    if board[i][j] == 'O':  # check if the 'O' in the edge
                        # find the path that start from the edge position
                        self.dfs(board, i, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '*'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)


a = Solution()
print(a.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print(a.solve([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]))
