class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can, con = 0, 0
        # for n in nums:
        #     if con == 0:
        #         can = n
        #     if can == n:
        #         con += 1
        #     else:
        #         con -= 1
        # return can

        major, count = 0, 0
        for n in nums:
            if count == 0:
                count += 1
                major = n
            elif major == n:
                count += 1
            else:
                count -= 1
        return major

    # dict
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        length = len(nums)
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > length // 2:
                return n

    def majorityElement_II(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = set()
        # d = {}
        # for n in nums:
        #     d[n] = d.get(n, 0) + 1
        #     if d[n] > len(nums) //3:
        #         res.add(n)
        # return list(res)

        count1, count2, major1, major2 = 0, 0, 0, 1
        for n in nums:
            if major1 == n:
                count1 += 1
            elif major2 == n:
                count2 += 1
            elif count1 == 0:
                count1, major1 = 1, n
            elif count2 == 0:
                count2, major2 = 1, n
            else:
                count1, count2 = count1 - 1, count2 - 1
        # select the most frequency 2 numbers and compare if the number is greater than
        # n/3
        return [n for n in (major1, major2)
                if nums.count(n) > len(nums) // 3]
