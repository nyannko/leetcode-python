class Solution(object):

    # exactly
    def can_jump(self, arr):
        index = 0
        length = len(arr)
        while index < length:
            step = arr[index]
            index = index + step

            if index >= len(arr) - 1:
                return True
            elif index < len(arr) - 1:
                if step == 0:
                    return False

    def jump_game_start(self, nums):
        reach = 0
        i = 0
        while i <= reach < len(nums) - 1:
            index = i + nums[i]
            reach = max(reach, index)
            i = i + 1
        return reach >= len(nums) - 1

    def jump_game_end(self, nums):
        length = len(nums) - 1
        left_most_index = length
        i = length - 1
        while i >= 0:
            if i + nums[i] >= left_most_index:
                left_most_index = i
            i -= 1
        return left_most_index == 0

    def jump_game_dp(self, nums):
        arr = []
        arr.insert(0, 0)
        for i, item in enumerate(nums):
            if i < 1: continue
            arr.insert(i, max(arr[i - 1], nums[i - 1]) - 1)
            if arr[i] < 0: return False
        return True

    def jump(self, nums):
        result = last = cur = 0
        for i, j in enumerate(nums):
            if i > last:
                last = cur
                result += 1
            cur = max(cur, i + nums[i])
        return result
