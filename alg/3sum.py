class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            print(i, v, nums, nums[:-2])
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
        for x in nums[i + 1:]:
                print(x)
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))

        return res


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
