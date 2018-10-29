class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for e in emails:
            local, domain = e.split('@')
            local_plus = local.split('+')[0]
            local_dot = ''.join(local_plus.split('.'))
            res.add('@'.join([local_dot, domain]))
        return len(res)
