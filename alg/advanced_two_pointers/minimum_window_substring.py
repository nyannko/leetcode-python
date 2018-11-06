class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        head, begin, end = 0, 0, 0
        min_length = float('inf')

        counter = len(t)

        from collections import defaultdict
        d = defaultdict(int)
        for i in t:
            d[i] += 1

        while end < len(s):
            if d[s[end]] > 0:
                counter -= 1
            d[s[end]] -= 1
            end += 1

            # all letters in t has occurred in the window
            while counter == 0:
                # clac length
                if end - begin < min_length:
                    head = begin
                    min_length = end - begin

                # remove a letter in t from window
                if d[s[begin]] == 0:
                    counter += 1
                d[s[begin]] += 1
                begin += 1

        return '' if min_length == float('inf') \
            else s[head:head + min_length]
