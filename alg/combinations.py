class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # nums = [x for x in range(1, n + 1)]
        # print(nums)
        result = []
        path = []
        step = 1
        self.dfs(n, k, step, path, result)
        return result

    def dfs(self, n, k, start, path, result):
        if k == len(path):
            result.append(path)
            return

        for i in range(start, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, list(path), result)
            path.pop()


a = Solution()
print(a.combine(4, 2))
