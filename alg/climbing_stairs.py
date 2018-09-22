class Solution:
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        path = []
        step = 0
        self.dfs(n, step, path, res)
        return len(res)

    def dfs(self, n, step, path, res):
        if n < 0: return
        if n == 0:
            res.append(path)
            return

        for i in [1, 2]:
            self.dfs(n - i, step + 1, path + [i], res)

    def climbStairs(self, n):
        a = b = 1
        res = []
        for _ in range(n):
            a, b = b, b + a
            res.append(a)
        print(res)
        return a

    def climbStairs2(self, n):
        res = []
        res.append(1)
        res.append(1)
        for i in range(2, n):
            res.append(res[i - 1] + res[i - 2])
        print(res)
    # 1,1,2,3
    #   2,1


a = Solution()
print(a.climbStairs(5))
