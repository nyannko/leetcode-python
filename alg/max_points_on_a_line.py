from collections import defaultdict
from decimal import Decimal


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        d = defaultdict(int)
        result = 0
        for i in range(0, len(points)):
            d.clear()  # clear dict for each round
            cur_max, overlap = 0, 0
            for j in range(i + 1, len(points)):
                dx, dy = points[j].x - points[i].x, \
                         points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.getGCD(dx, dy)  # get the common greatest divisor
                dx //= gcd
                dy //= gcd  # decrease the x and y at the same time to prevent overflow
                d[(dx, dy)] += 1
                print(d)
                cur_max = max(cur_max, d[(dx, dy)])
            result = max(result, cur_max + overlap + 1)

        return result

    def getGCD(self, i, j):
        if j == 0: return i
        return self.getGCD(j, i % j)

    def maxPoints2(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        result = 0
        d = defaultdict(int)
        for i in range(0, len(points)):
            d.clear()
            overlap, cur_max = 0, 0
            for j in range(i + 1, len(points)):
                dx, dy = points[j].x - points[i].x, \
                         points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                slope = Decimal(dy * 1.0) / dx if dx != 0 else 'infinity'
                d[slope] += 1
                print(i, j, points[i].x, points[i].y, points[j].x, points[j].y, dx, dy, d)  # for debug
                cur_max = max(cur_max, d[slope])
            result = max(result, cur_max + overlap + 1)
        return result


a = Solution()
l = [[0, 0], [1, 0], [1, 1], [2, 2]]
# l = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
# ↑ in this case maxPoints2 will fail because of the floating point precision..{0.9999999894638303: 2}
# l = [[84, 250], [0, 0], [1, 0], [0, -70], [0, -70], [1, -1], [21, 10], [42, 90], [-42, -230]]
input = [Point(i, j) for i, j in l]
print(a.maxPoints(input))
