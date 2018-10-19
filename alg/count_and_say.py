class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            let, tmp, count = s[0], '', 0
            for c in s:
                if let == c:
                    count += 1
                else:
                    tmp += str(count) + let
                    let = c
                    count = 1
            tmp += str(count) + let
            s = tmp
        return s
