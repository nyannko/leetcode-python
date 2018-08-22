import unittest

from pow import Solution


class test_pow(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_check_pow_loop(self):
        self.assertEqual(self.obj.check_pow_loop(2, 3), 8)
        self.assertEqual(self.obj.check_pow_loop(2, -4), 1 / 16)

    def test_recursive(self):
        self.assertEqual(self.obj.check_recursive(2, 3), 8)
        self.assertEqual(self.obj.check_recursive(2, -5), 1 / 32)

    def test_pow_basic_recursive(self):
        self.assertEqual(self.obj.check_power_recursive(2, 3), 8)
        self.assertEqual(self.obj.check_power_recursive(2, -4), 1 / 16)

    def test_check_pow_recorsive2(self):
        self.assertEqual(self.obj.check_power_recorsive2(2, 3), 8)
        self.assertEqual(self.obj.check_power_recorsive2(2, -4), 1 / 16)
        self.assertEqual(self.obj.check_power_recorsive2(1, 1000000000000), 1)
        self.assertEqual(self.obj.check_power_recorsive2(1, -1000000000000), 1)
