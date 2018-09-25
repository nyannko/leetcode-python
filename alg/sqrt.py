class Solution:
    def mySqrt(self, x):
        left = 1
        right = x / 2
        last_mid = 0

        if x < 2:
            return x

        while left <= right:
            mid = left + (right - left) // 2
            if x / mid > mid:
                left = mid + 1
                last_mid = mid
            elif x / mid < mid:
                right = mid - 1
            else:
                return mid

        return last_mid


a = Solution()
print(a.mySqrt(8))
