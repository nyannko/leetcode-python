class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        N = 0
        for i, v in enumerate(S):
            N = N * int(v) if v.isdigit() else N + 1
            if K <= N: break
        # print "N", N, i
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N = N / int(c)
                # print N, K, c
                K = K % N
                # print K
            else:
                if K == 0 or K == N:
                    # print K, N
                    return c
                # print K, N
                N -= 1
