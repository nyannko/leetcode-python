class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            first, last = 0, len(i) - 1
            while first <= last:
                mid = (first + last) // 2
                if i[mid] == target: return True
                if i[mid] < target:
                    first = mid + 1
                if i[mid] > target:
                    last = mid - 1
        return False
