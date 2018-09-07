class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        step = 0
        candidates.sort()
        self.dfs(candidates, target, path, step, res)
        return res

    def dfs(self, candidates, target, path, step, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(step, len(candidates)):
            self.dfs(candidates, target - candidates[i], path + [candidates[i]], i, res)


a = Solution()
print(a.combinationSum([2, 3, 6, 7], 7))
# https://pasteboard.co/HCPWD1t.png
