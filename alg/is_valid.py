class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in d.keys():
                stack.append(char)
            elif char in d.values():
                if stack == [] or char != d[stack.pop()]:
                    return False
            else:
                return False
        return stack == []
        # 复习is ==....


a = Solution()
print(a.isValid("[])"))
