class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for _ in range(len(ratings))]
        inc = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                inc += 1
                candy[i] = max(candy[i], inc)
            else:
                inc = 1

        inc = 1
        for i in range(len(ratings) - 1)[::-1]:
            if ratings[i] > ratings[i + 1]:
                inc += 1
                candy[i] = max(candy[i], inc)
            else:
                inc = 1
        return sum(candy)
