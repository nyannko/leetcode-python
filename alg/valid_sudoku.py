class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for x in range(9):
                        if x != i and board[x][j] == board[i][j]:
                            return False

                    for y in range(9):
                        if y != j and board[i][y] == board[i][j]:
                            return False

                    for x in range(3 * (i // 3), 3 * (i // 3 + 1)):
                        for y in range(3 * (j // 3), 3 * (j // 3 + 1)):
                            if (x != i or y != j) and board[x][y] == board[i][j]:
                                return False
        return True


a = Solution()
print(a.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
