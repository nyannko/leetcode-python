class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque  # append, popleft, len
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        len1, len2 = len(self.q1), len(self.q2)
        if len1 > len2:  # len2 == 0
            for _ in range(len1 - 1):
                ele = self.q1.popleft()
                self.q2.append(ele)
            return self.q1.popleft()
        if len2 > len1:  # len1 == 0
            for _ in range(len2 - 1):
                ele = self.q2.popleft()
                self.q1.append(ele)
            return self.q2.popleft()
        # else: #len1 == len2 == 0 exception

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        len1, len2 = len(self.q1), len(self.q2)
        if len1 > len2:
            return self.q1[-1]
        elif len1 < len2:
            return self.q2[-1]
        else:
            return []

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.q1 and not self.q2:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
