class Solution:
    def trap(self, height):
        i, j = 0, len(height) - 1
        l_max, r_max = 0, 0
        max_value = 0
        while i <= j:
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[j])
            if l_max < r_max:
                max_value += l_max - height[i]
                i += 1
            else:
                max_value += r_max - height[j]
                j -= 1
        return max_value


a = Solution()
print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
