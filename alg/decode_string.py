class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # long and ugly
        stack = []
        for i in s:
            # print(stack)
            if i.isdigit():
                stack.append(i)
            elif i.isalpha():
                stack.append(i)
            elif i == '[':
                nums = []
                while stack and stack[-1].isdigit():
                    nums.append(stack.pop())
                num = ''.join(nums[::-1])
                stack.append(num)
                stack.append('[')
            elif i == ']':
                alpha = []
                while stack and stack[-1].isalpha():
                    alpha.append(stack.pop())
                c = ''.join(alpha[::-1])
                stack.pop()  # pop '['
                num = int(stack.pop())
                stack.append(num * c)
        # return stack
        return ''.join(stack)
