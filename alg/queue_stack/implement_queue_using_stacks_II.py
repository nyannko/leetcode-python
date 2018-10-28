class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque  # append, pop, len
        self._stack = deque()
        self.res = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        s = self._stack
        # pop all elements from original stack
        while s:
            ele = s.pop()
            self.res.append(ele)
        # append new element
        s.append(x)
        # append back
        while self.res:
            ele = self.res.pop()
            s.append(ele)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not len(self._stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
