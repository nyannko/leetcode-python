import unittest

from alg.max_area import Solution

class TestMaxArea(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_max_area(self):
        arr1 = [1,1]
        self.assertEqual(self.obj.max_area(arr1), 1)