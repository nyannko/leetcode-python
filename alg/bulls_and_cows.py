class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # slow
        n = len(secret)
        bull, cow = 0, 0
        num = [0 for _ in range(10)]  # 10 nums
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if num[int(secret[i])] < 0:
                    cow += 1
                if num[int(guess[i])] > 0:
                    cow += 1
                num[int(secret[i])] += 1
                num[int(guess[i])] -= 1
        return "{}A{}B".format(bull, cow)

    def getHint1(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import operator
        bull = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return "{}A{}B".format(bull, both - bull)


a = Solution()
a.getHint("112333", "011111")
a.getHint("7810", "0817")
a.getHint("1011", "0100")
