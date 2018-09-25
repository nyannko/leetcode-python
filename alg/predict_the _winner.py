class Solution(object):
    def predict_the_winner(self, nums):
        length = len(nums)
        cache = [[-1 for x in range(length)] for x in range(length)]

        def predict(start, end, turn):
            if cache[start][end] == -1:

                # base case
                if start == end:
                    if turn is True:
                        r = nums[start]
                    else:
                        r = 0

                    # recursion
                else:
                    if turn is True:
                        r = max(nums[start] + predict(start + 1, end, False),
                                nums[end] + predict(start, end - 1, False))
                    else:
                        r = min(predict(start + 1, end, True), predict(start, end - 1, True))

                cache[start][end] = r

            return cache[start][end]

        return predict(0, len(nums) - 1, True)

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        player = {0: 0, 1: 0}
        l = 0
        r = len(nums) - 1
        turn = 0
        while l <= r:
            if nums[l] >= nums[r]:
                score = nums[l]
                l += 1
            else:
                score = nums[r]
                r -= 1

            if turn == 0:
                player[0] += score
                turn = 1
            elif turn == 1:
                player[1] += score
                turn = 0

        print(player)

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 递归函数
        def predict(start, end, turn):
            if cache[start][end] == -1:  # 查找cache, 如果里面没有值，就开始递归，如果有就直接返回
                if start == end:  # base case: Player 1优先选择数字
                    r = nums[start] if turn else 0  # if turn is True: r = nums[start] else r = 0
                else:  # 递归
                    if turn:  # 轮到player1: 选择头部或者尾部的值+之前得到的最大值
                        r = max(nums[start] + predict(start + 1, end, False),
                                nums[end] + predict(start, end - 1, False))
                    else:  # 轮到player2: 选择之前得到的最小值
                        r = min(predict(start + 1, end, True), predict(start, end - 1, True))
                cache[start][end] = r  # 存入cache
            return cache[start][end]

        n = len(nums)
        cache = [[-1 for i in range(n)] for j in range(n)]  # 初始化cache
        return 2 * predict(0, len(nums) - 1, True) >= sum(nums)  # 递归函数入口,返回时判断player1 > player2


arr1 = [1, 5, 2]
arr2 = [1, 5, 233, 7]
arr3 = [6, 0, 233, 5]
a = Solution()
b = a.predict_the_winner(arr2)
print(b)
