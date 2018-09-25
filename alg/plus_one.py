class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = str(int(''.join(map(str, digits))) + 1)
        return [int(s) for s in num]

    def plusOne1(self, digits):
        num = 0
        for i, v in enumerate(digits):
            print((len(digits) - 1 - i))
            num += v * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]


a = Solution()
print(a.plusOne1([4, 3, 2, 1]))
