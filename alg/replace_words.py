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
        # why that does not work?
        # l =  sentence.split()
        # for i, v in enumerate(l):
        #     for j in dict:
        #         if v.startswith(j):
        #             l[i] = j
        # return ' '.join(l)

        l = sentence.split()
        for i in range(len(l)):
            for j in dict:
                if l[i].startswith(j):
                    l[i] = j
        return " ".join(l)
