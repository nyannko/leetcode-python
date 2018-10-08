class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used = dict.fromkeys(nums, False)
        print(used)
        longest = 0
        for i in range(len(nums)):
            if used[nums[i]]: continue
            length = 1

            j = nums[i] + 1
            while j in used:
                used[j] = True
                length += 1
                j += 1

            m = nums[i] - 1
            while m in used:
                used[m] = True
                length += 1
                m -= 1
            longest = max(longest, length)
        return longest
