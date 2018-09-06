import unittest

from alg.triangle import Solution


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_minimum_total(self):
        arr1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        arr2 = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(self.obj.minimum_total(arr1), 11)
        self.assertEqual(self.obj.minimum_total(arr2), 7)
