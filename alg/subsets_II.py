class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        path = []
        step = 0

        self.start(nums, step, path, result)
        return result

    def start(self, nums, step, path, result):
        result.append(path)
        # print(path)
        for i in range(step, len(nums)):
            print(i)
            if i != step and nums[i] == nums[i - 1]: continue
            self.start(nums, i + 1, [nums[i]] + path, result)

    # todo
    def subsetsWithDup1(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # print(d)

        elems = []
        for i, v in d.items():
            elems.append([i, v])
        # print(elems)

        path = []
        result = []
        step = 0

        self.start1(elems, step, path, result)
        return result

    # todo
    def start1(self, nums, step, path, result):
        if step == len(nums):
            # print(path)
            result.append(path)
            return

        print(nums[step][1])
        for i in range(nums[step][1]):
            for j in range(i):
                path.append(nums[step][0])
                # print(path)
            self.start1(nums, step + 1, list(path), result)
            # for j in range(i):
            #     path.pop()

    # complicated..
    def subsetsWithDup2(self, nums):
        nums.sort()
        result = []
        selected = {}

        # list way
        # count = [0 for _ in range(nums[-1] - nums[0] + 1)]

        # dict way, faster than list
        length = nums[-1] - nums[0] + 1
        keys = [x for x in range(length)]
        count = dict.fromkeys(keys, 0)
        # print(count)

        # list way
        # for i in nums:
        #     num = i - nums[0]
        #     print(i, num)
        #     count[num] += 1

        # dict way
        for i in nums:
            num = i - nums[0]
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # print(count)
        self.start2(nums, count, selected, 0, result)

        return result

    def start2(self, nums, count, selected, step, result):
        if step == len(count):
            print(selected)
            subset = []
            for i, v in selected.items():
                for j in range(v):
                    subset.append(i + nums[0])
            result.append(subset)
            # print(result)
            return
        # step is a increment counter, len(count) is the boundary, count(step) is the frequency of numbers
        for i in range(count[step] + 1):
            # print(i)
            selected[step] = i
            self.start2(nums, count, selected, step + 1, result)

    def subsetsWithDup3(self, nums):
        elem = {}
        for i in nums:
            num = i - nums[0]
            if num in elem:
                elem[num] += 1
            else:
                elem[num] = 1

        elem = sorted(elem.items())
        print(elem)

        path = []
        result = []
        step = 0
        self.start3(nums, elem, step, path, result)
        return result

    def start3(self, nums, elem, step, path, result):
        if step == len(elem):
            result.append(path)
            return
        # print(nums[0])
        for i in range(elem[step][1] + 1):
            for j in range(i):
                print(i, j)
                path.append(elem[step][0] + nums[0])
            # print(path)
            self.start3(nums, elem, step + 1, list(path), result)
            for _ in range(i):
                print("pop", path.pop())

    def subsetsWithDup4(self, nums):
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
            # del duplicated tuple, cannot add list to set since it's mutable
            # but really slow..
            tuples = {tuple(x) for x in result}
            real_res = [list(x) for x in tuples]
        return real_res


a = Solution()
print(a.subsetsWithDup2([1, 2, 2]))
