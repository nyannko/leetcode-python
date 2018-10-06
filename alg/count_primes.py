class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_prime = [False] * n
        # print not_prime
        count = 0
        for i in range(2, n):
            if not_prime[i] is False:
                count += 1
                for j in range(2, n):
                    if i * j < n:
                        not_prime[i * j] = True
                    else:
                        break
        return count
