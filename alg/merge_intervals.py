# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Convert to a list
        intervals = [[intervals[e].start, intervals[e].end] for e in range(len(intervals))]
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1] <= intervals[i][1]:
                intervals[i - 1][1] = intervals[i][1]
                del intervals[i]
            elif intervals[i - 1][1] > intervals[i][1]:
                del intervals[i]
            # After merging, the latter Interval has the same index as the removed one, so index does not change.
            # Only when these Intervals do not merge, index increase.
            else:
                i += 1
        return intervals

    def merge1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # res[] <---(add)--- intervals[...]
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(i.end, res[-1].end)
            else:
                res += i,
        return res


a = Solution()
# help(Solution)
print(a.merge1([Interval(0, 5), Interval(5, 7)]))  # [[0, 7]]
print(a.merge1([Interval(0, 5), Interval(2, 5)]))  # [[0, 5]]
print(a.merge1([Interval(1, 4), Interval(0, 2), Interval(3, 5)]))  # [[0, 5]]
print(a.merge1([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))  # [[1, 6], [8, 10], [15, 18]]
