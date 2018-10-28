class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu = [0]
        for i in nums:
            self.accu.append(self.accu[-1] + i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]
        # return sum(self.nums[:j+1]) - sum(self.nums[:i])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
