class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        i = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                if not stack:
                    area = heights[tp] * i
                else:
                    area = heights[tp] * (i - stack[-1] - 1)
                if res < area:
                    res = area

        while stack:
            tp = stack.pop()
            if not stack:
                area = heights[tp] * i
            else:
                area = heights[tp] * (i - stack[-1] - 1)
            if res < area:
                res = area
        return res
