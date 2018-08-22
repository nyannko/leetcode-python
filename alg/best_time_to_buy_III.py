class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        f = [0 for _ in range(length)]
        g = [0 for _ in range(length)]

        cur_min = prices[0]
        for i, v in enumerate(prices):
            if i < 1: continue
            f[i] = max(f[i-1], prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
            # cur_min = min(cur_min, prices[i])
            # f[i] = max(f[i-1], prices[i] - cur_min)
        peak = prices[length - 1]
        for i, v in reversed(list(enumerate(prices))):
            if i >= length - 1: continue
            peak = max(peak, prices[i])
            g[i] = max(g[i], peak - prices[i])

        p=0
        print(f, g)
        for i, v in enumerate(prices):
            p = max(f[i] + g[i], p)

        return p

a = Solution()
#print(a.maxProfit([3,3,5,0,0,3,1,4]))
print(a.maxProfit([5,3,2,6,4,7,1]))
