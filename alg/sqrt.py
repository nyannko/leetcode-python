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

    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        l, r = 0, x / 2 + 1
        while l <= r:
            m = (l + r) / 2
            if m ** 2 == x: return m  # if equals
            if m ** 2 < x:
                l = m + 1
            else:
                r = m - 1
        return l - 1  # lower bound


a = Solution()
print(a.mySqrt(8))
