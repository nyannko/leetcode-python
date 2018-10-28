class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # move element from q1 to q2, and pop the peek from q2
        self.peek()
        return self.q2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.q2:
            while self.q1:
                ele = self.q1.pop()
                self.q2.append(ele)
        return self.q2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.q1 and not self.q2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
