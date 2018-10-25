class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pass
        # notice 0..
        import sys
        pro, res = 1, -sys.maxsize
        for i in nums:
            pro *= i
            res = max(res, pro)
            if i == 0: pro = 1

        pro = 1
        for i in nums[::-1]:
            pro *= i
            res = max(res, pro)
            if i == 0: pro = 1

        return res

        # [2,3,-2,4]
        # [5,7,-1,3]
        # [3,-1,5,7]
        # [-2]
        # [-3,0,1,-2]
