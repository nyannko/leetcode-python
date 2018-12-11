class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = set()
        for w in A:
            even = ''.join(sorted(w[0::2]))
            odd = ''.join(sorted(w[1::2]))
            d.add((even, odd))
        return len(d)
