from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        # defaultdict
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        print(d.items())

        """ Counter
        cnt = Counter()
        for i in s:
            cnt[i] += 1
        print(cnt)
        """

        """ Normal
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        """

        d = sorted(d.items(), key=lambda a: a[1], reverse=True)
        print(d)
        new_str=''
        for i in d:
            new_str += i[0] * i[1]
        print(new_str)


a = Solution()
a.frequencySort('aabbcAa')