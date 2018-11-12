class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        l = sentence.split()
        # print(l)
        for i, v in enumerate(l):
            tmp = []
            res = []
            for j in dict:
                if v.startswith(j):
                    tmp.append(v)
                    res.append(j)
                    # print('k',tmp,res)
            if tmp:
                l[i] = res[tmp.index(min(tmp))]
        return ' '.join(l)

    def replaceWords1(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        l = sentence.split()
        # print(l)
        for i, v in enumerate(l):
            tmp = []
            res = []
            for j in dict:
                if v.startswith(j):
                    tmp.append(v)
                    res.append(j)
                    # print('k',tmp,res)
            if tmp:
                l[i] = res[tmp.index(min(tmp))]
        return ' '.join(l)
