class Solution:
    def findErrorNums1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ugly
        res, val = [], 0
        import operator
        from functools import reduce
        # for python2
        v1 = reduce(operator.xor, list(set(nums)) + nums)
        res.append(v1)
        l = list(set(nums))
        l.sort()
        # print l
        for i, v in enumerate(l):
            val ^= (i + 1) ^ v
            if val != 0:
                res.append(i + 1)
                break
        if len(res) == 1:
            res.append(l[-1] + 1)

        return res

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        # from collections import Counter
        # c = Counter(nums)
        # for k, v in c.items():
        #     if v == 2:
        #         res.append(k)
        #         break

        # 2 works fine
        # d = {}
        # for i in nums:
        #     if i in d:
        #         res.append(i)
        #         break
        #     else:
        #         d[i] = 1

        # 1 generate a dict TLE; maybe count has problems
        # d = {nums.count(i) : i for i in nums}
        # if 2 in d:
        #     res.append(d[2])

        nums_set = list(set(nums))
        v2 = sum(range(len(nums_set) + 2)) - sum(nums_set)
        res.append(v2)
        return res

    def findErrorNums3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]

    def findErrorNums4(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # fastest
        n = len(nums)
        sum1 = int((n ** 2 + n) / 2)
        sum2 = sum(set(nums))
        sum3 = sum(nums)
        return [sum3 - sum2, sum1 - sum2]

# https://leetcode.com/problems/find-the-duplicate-number/
# https://leetcode.com/problems/missing-number/
