class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stack, res = [], []

        for i in nums:
            while len(stack) and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)

        for i in findNums:
            res.append(d.get(i, -1))
        return res
        # return map(lambda x: d.get(x, -1)), findNums
