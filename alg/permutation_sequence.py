import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n + 1))
        print(numbers)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            print(n, k, math.factorial(n))  # 4*3*2*1
            index, k = divmod(k, math.factorial(n))
            print(index, k)
            print(str(numbers[index]))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


a = Solution()
print(a.getPermutation(2, 1))
