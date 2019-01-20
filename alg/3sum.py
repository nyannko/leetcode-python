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

    def threeSum1(self, nums):
        res = []
        nums.sort();
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
