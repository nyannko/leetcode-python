class Solution(object):
    def max_area(self, height):
        start = 0
        end = len(height) - 1
        result = 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            result = max(result, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return result
