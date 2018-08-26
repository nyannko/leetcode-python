class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        path = []
        self.dfs(nums, path, result)
        return result

    def dfs(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path)
            return

        for i in nums:
            try:
                path.index(i)
                # print(pos)
            except:
                path.append(i)
                # print(path)
                self.dfs(nums, list(path), result)
                path.pop()


a = Solution()
print(a.permute([1, 2, 3]))
