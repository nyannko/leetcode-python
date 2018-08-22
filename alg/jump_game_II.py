class Solution(object):

    def jump(self, nums):
        result = last = cur = 0
        for i, j in enumerate(nums):
            if i > last:
                last = cur
                result += 1
            cur = max(cur, i + nums[i])
        return result
