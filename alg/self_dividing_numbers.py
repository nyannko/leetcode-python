class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # ugly
        l = list(range(left, right + 1))

        for i in l[:]:
            d = list(str(i))  # ['1', '4']
            print(d)
            if '0' in d:
                l.remove(i)
                continue
            res = [i % m for m in map(int, d) if i % m != 0]
            res_len = len(res)
            if res_len:
                l.remove(i)
        return l
