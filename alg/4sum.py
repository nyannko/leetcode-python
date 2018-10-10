class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.find_nsum(nums, target, 4, [], result)
        return result

    def find_nsum(self, nums, target, step, path, result):
        if len(nums) < step or step < 2: return
        if step == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] - target
                if s == 0:
                    result.append(path + [nums[l], nums[r]])
                    # print(result)
                    l += 1;
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - step + 1):
                # print(nums[i] * step, nums[-1] + step)
                if target < nums[i] * step or target > nums[-1] * step: break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    self.find_nsum(nums[i + 1:], target - nums[i], step - 1, path + [nums[i]], result)
        return
