import unittest
from alg.sell_stock import Solution


class TestSellStock(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_max_profit(self):
        arr1 = [10, 5, 3, 7, 6, 4]
        arr2 = [10, 5, 3, 7, 1, 4, 2]
        self.assertEqual(self.obj.max_profit(arr2), 4)
        self.assertEqual(self.obj.max_profit(arr1), 4)

    def test_max_profit_II(self):
        arr1 = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.obj.max_profit_II(arr1), 7)
