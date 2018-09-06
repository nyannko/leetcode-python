import unittest

from alg.jump_game_II import Solution


class TestJumpGameII(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_jump(self):
        arr = [2, 3, 1, 1, 4]
        arr1 = [2, 3, 1, 1, 4, 6, 1, 0, 0, 3, 5, 2, 1]
        arr2 = [1,2,3]
        arr3 = [1, 2]
        arr4 = [5,9,3,2,1,0,2,3,3,1,0,0]
        self.assertEqual(self.obj.jump(arr), 2)
        self.assertEqual(self.obj.jump(arr1), 5)
        self.assertEqual(self.obj.jump(arr2), 2)
        self.assertEqual(self.obj.jump(arr4), 3)
        self.assertEqual(self.obj.jump(arr3), 1)



