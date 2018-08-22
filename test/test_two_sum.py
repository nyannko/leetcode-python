import unittest

from code.two_sum import Solution


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_two_sum(self):
        nums = [1, 3, 4, 6]
        target = 10
        self.assertEqual(self.obj.two_sum(nums, target), (2, 3))

    def test_two_pass_dict(self):
        nums = [5, -2, 3, 7, 9]
        target = 3
        self.assertEqual(self.obj.two_pass_dict(nums, target), (0, 1))

    def test_one_pass_dict(self):
        nums = [5, -2, 3, 7, 9]
        target = 3
        self.assertEqual(self.obj.one_pass_dict(nums, target), (0, 1))
