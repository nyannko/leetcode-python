class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        # check if the new matrix valid
        if row * col != r * c:
            return nums

        # create a new matrix
        matrix = [[0 for _ in range(c)] for _ in range(r)]

        # flat original matrix
        flat_nums = [i for row in nums for i in row]

        # assgn new number, ugly here..
        counter = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = flat_nums[counter]
                counter += 1
        return matrix
