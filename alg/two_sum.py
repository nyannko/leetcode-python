class Solution(object):

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                sum = nums[i] + nums[j]
                if sum == target:
                    return i, j

    def two_pass_dict(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i

        for i, num in enumerate(nums):
            j = target - num
            if j in dic and dic[j] != i:
                return i, dic[j]

    def one_pass_dict(self, nums, target):
        """
        :param nums:  List[int]
        :param target: int
        :return: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in dic:
                return dic[j], i
            dic[num] = i
