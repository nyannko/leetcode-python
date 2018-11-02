class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        c = collections.Counter()
        for d in cpdomains:
            n, d = d.split()
            length = d.count('.') + 1
            for i in range(length):
                c[d.split('.', i)[i]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]
