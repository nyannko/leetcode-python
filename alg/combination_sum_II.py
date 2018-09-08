class Solution(object):
    def combinationSum2(self, candidates, target):
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
        pre = -1
        for i in range(step, len(candidates)):
            if pre == candidates[i]: continue
            pre = candidates[i]
            self.dfs(candidates, target - candidates[i], path + [candidates[i]], i + 1, res)


a = Solution()
print(a.combinationSum2([2,5,2,1,2], 5))
#https://pasteboard.co/HCXDtTs.png
#https://pasteboard.co/HCXK1Y3.png
