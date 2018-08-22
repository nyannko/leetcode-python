import unittest
from longest_substring import Solution

class Testsubstring(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_len_longest_substring(self):
        arr1 = "abcabcbb"
        arr2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
        self.assertEqual(self.obj.substring(arr1), 3)
        self.assertEqual(self.obj.substring(arr2), 95)