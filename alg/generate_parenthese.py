class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(p, left, right, result=[]):
            if left > 0:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                print(p)
                result.append(p)
            return result

        return generate('', n, n)


a = Solution()
print(a.generateParenthesis(3))
