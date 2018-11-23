class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # filter(lambda x : x[x.find(" ") + 1].isdigit(), logs)
        # fast
        d = filter(lambda x: x.split()[1].isdigit(), logs)
        l = filter(lambda x: x.split()[1].isalpha(), logs)
        # l = filter(lambda x : x[x.find(" ") + 1].isalpha(), logs)
        # slow
        # d = [i for i in logs if i[i.find(" ") + 1].isdigit()]
        # l = [i for i in logs if i[i.find(" ") + 1].isalpha()]
        # l.sort(key = lambda x: (x[x.find(" "):]))
        l.sort(key=lambda x: x.split(" ", 1)[1])
        return l + d
