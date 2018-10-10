class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        # if self.stack:
        self.min_stack.pop()
        return self.stack.pop()
        # else:
        # return None

    def top(self):
        """
        :rtype: int
        """
        # if self.stack:
        return self.stack[-1]
        # else:
        # return None

    def getMin(self):
        """
        :rtype: int
        """
        # if self.min_stack:
        return self.min_stack[-1]
        # else:
        # return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
