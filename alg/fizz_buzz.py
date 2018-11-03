class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not bool(i % 3)) + 'Buzz' * (not bool(i % 5)) or str(i) for i in range(1, n + 1)]

    class Solution(object):
        def fizzBuzz1(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            res = []
            for i in range(1, n + 1):
                if i % 15 == 0:
                    res.append("FizzBuzz")
                elif i % 3 == 0:
                    res.append("Fizz")
                elif i % 5 == 0:
                    res.append("Buzz")
                else:
                    res.append(str(i))
            return res
