class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = nums[-1] - nums[0] + 1
        # why 2? stupid..
        l = [x for x in range(length)]
        print(l)
        d = dict.fromkeys(l, 0)
        print(d)
        for i in nums:
            num = i - nums[0]
            if num in d:
                d[num] += 1
            else:
                d[num] = 0

        print(d)

        result = []
        path = []

        self.dfs(nums, d, path, result)

        return result

    def dfs(self, nums, d, path, result):
        if len(nums) == len(path):
            path = list(map(lambda x: x + nums[0], path))
            result.append(path)
            return

        for i, v in d.items():
            count = 0
            for j in path:
                if i == j:
                    count += 1
            if count < v:
                path.append(i)
                # print(path)
                self.dfs(nums, d, list(path), result)
                path.pop()


a = Solution()
print(a.permuteUnique([1, 2, 2]))
