class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        global d
        d = {0: ' ', 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        step = 0
        path = []
        result = []
        self.dfs(digits, path, step, result)
        return result

    def dfs(self, digits, path, step, result):
        if len(digits) == step:
            result.append(''.join(path))
            return

        for i in d[int(digits[step])]:
            self.dfs(digits, path + list(i), step + 1, result)


a = Solution()
print(a.letterCombinations("23"))
