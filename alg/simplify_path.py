class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        path = path.split('/')
        path = [i for i in path if i != '' and i != '.']
        for i in path:
            if i != '..':
                res.append(i)
            elif res:
                res.pop()
            # if res and i == '..':
            #     res.pop()
        # print(path, res)
        print('/' + '/'.join(res))


a = Solution()
a.simplifyPath('/a//b////c/d//././/..')
