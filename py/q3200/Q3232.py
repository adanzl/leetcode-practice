"""
 * 给你一个 正整数 数组 nums。
 * 小红和小明正在玩游戏。在游戏中，小红可以从 nums 中选择所有个位数 或 所有两位数，剩余的数字归小明所有。
 * 如果小红所选数字之和 严格大于 小明的数字之和，则小红获胜。
 * 如果小红能赢得这场游戏，返回 true;否则，返回 false。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 99
 * 链接：https://leetcode.cn/problems/find-if-digit-game-can-be-won/
"""
from typing import List


class Solution:

    def canAliceWin(self, nums: List[int]) -> bool:
        sum1, sum2 = 0, 0
        for num in nums:
            if num > 9:
                sum2 += num
            else:
                sum1 += num
        return sum1 != sum2


if __name__ == '__main__':
    # False
    print(Solution().canAliceWin([1, 2, 3, 4, 10]))
    # True
    print(Solution().canAliceWin([1, 2, 3, 4, 5, 14]))
    # True
    print(Solution().canAliceWin([5, 5, 5, 25]))
