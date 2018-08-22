import unittest

from jump_game import Solution


class TestJumpGame(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def tearDown(self):
        del self.obj

    def test_jump_game(self):
        arr1 = [2, 3, 1, 1, 4]
        arr2 = [3, 2, 1, 0, 4]
        self.assertEqual(self.obj.can_jump(arr1), True)
        self.assertEqual(self.obj.can_jump(arr2), False)

    def test_jump_game_start(self):
        arr1 = [2, 3, 1, 1, 4]
        arr2 = [3, 2, 1, 0, 4]
        self.assertEqual(self.obj.jump_game_start(arr1), True)
        self.assertEqual(self.obj.jump_game_start(arr2), False)

    def test_jump_game_send(self):
        arr1 = [2, 3, 1, 1, 4]
        arr2 = [3, 2, 1, 0, 4]
        arr3 = [1]
        self.assertEqual(self.obj.jump_game_end(arr1), True)
        self.assertEqual(self.obj.jump_game_end(arr2), False)
        self.assertEqual(self.obj.jump_game_end(arr3), True)

    def test_jump_game_dp(self):
        arr1 = [2, 3, 1, 1, 4]
        arr2 = [3, 2, 1, 0, 4]
        self.assertEqual(self.obj.jump_game_dp(arr1), True)
        self.assertEqual(self.obj.jump_game_dp(arr2), False)

    def test_jump(self):
        arr = [2, 3, 1, 1, 4]
        arr1 = [2, 3, 1, 1, 4, 6, 1, 0, 0, 3, 5, 2, 1]
        arr2 = [1, 2, 3]
        arr3 = [1, 2]
        arr4 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
        self.assertEqual(self.obj.jump(arr), 2)
        self.assertEqual(self.obj.jump(arr1), 5)
        self.assertEqual(self.obj.jump(arr2), 2)
        self.assertEqual(self.obj.jump(arr4), 3)
        self.assertEqual(self.obj.jump(arr3), 1)
