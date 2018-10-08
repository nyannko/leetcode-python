class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1)
        r = len(nums2)
        i, j = 0, 0
        arr = []

        while i < l and j < r:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        while i < l:
            arr.append(nums1[i])
            i += 1

        while j < r:
            arr.append(nums2[j])
            j += 1

        # print(arr, len(arr))
        size = len(arr)
        if size % 2 != 0:
            index = (size + 1) // 2
            return arr[index - 1]
        else:
            index = size // 2
            return (arr[index - 1] + arr[index]) / 2
