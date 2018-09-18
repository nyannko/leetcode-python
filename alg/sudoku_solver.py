class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.a(board)
        # print(board)

    def a(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(9):
                        board[i][j] = str(1 + k)
                        if self.isValid(board, i, j) and self.a(board):
                            return board
                        board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        for i in range(3 * (x // 3), 3 * (x // 3 + 1)):
            for j in range(3 * (y // 3), 3 * (y // 3 + 1)):
                if (i != x or j != y) and board[i][j] == board[x][y]:
                    return False
        return True


a = Solution()
s = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# print(a.isValid(s))
a.solveSudoku(s)
