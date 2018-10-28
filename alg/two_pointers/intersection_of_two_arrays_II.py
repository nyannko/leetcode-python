class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            print(p1, p2)
            if nums1[p1] > nums2[p2]:
                p2 += 1
            # if and elif are different; elif won't be evaluated..
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res

    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(nums1)
        res = []
        # n[nonexist_num] = 0
        for i in nums2:
            if counter[i] > 0:
                res.append(i)
                counter[i] -= 1
        return res
