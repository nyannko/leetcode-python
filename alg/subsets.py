class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        self.start(nums, [], 0, result)
        print(result)
        return result

    def start(self, nums, path, step, result):
        result.append(path)
        print(path)
        for i in range(step, len(nums)):
            self.start(nums, [nums[i]] + path, i + 1, result)

    def subsets1(self, nums):
        nums = sorted(nums)
        result = []
        selected = [False for _ in range(len(nums))]
        step = 0
        self.start1(nums, selected, step, result)
        return result

    def start1(self, nums, selected, step, result):
        if step == len(nums):
            f = []
            for i, v in enumerate(nums):
                if selected[i] is True:
                    f.append(v)
            result.append(f)
            print(step, selected, f, result)
            return

        selected[step] = True
        self.start1(nums, selected, step + 1, result)

        selected[step] = False
        self.start1(nums, selected, step + 1, result)

    def subsets2(self, nums):
        step = 0
        path = []
        result = []
        nums = sorted(nums)
        self.start2(nums, path, step, result)
        return result

    def start2(self, nums, path, step, result):
        if len(nums) == step:
            result += [path]
            return

        # 注意生成一个新列表。。。。。
        self.start2(nums, list(path), step + 1, result)

        path.append(nums[step])
        self.start2(nums, list(path), step + 1, result)

    # beat 100%
    def subsets3(self, nums):
        nums = sorted(nums)
        length = len(nums)
        result = []

        for i in range(1 << length):
            l = list()
            for j in range(length):
                if i & (1 << j) != 0:
                    l.append(nums[j])
            result.append(l)
            del l
        return result


a = Solution()
print(a.subsets3([3, 2, 4, 1]))
