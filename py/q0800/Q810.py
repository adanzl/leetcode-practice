"""
 * 黑板上写着一个非负整数数组 nums[i] 。
 * Alice 和 Bob 轮流从黑板上擦掉一个数字，Alice 先手。如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。 
 * 另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为 0。
 * 并且，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0 ，这个玩家获胜。
 * 假设两个玩家每步都使用最优解，当且仅当 Alice 获胜时返回 true。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] < 2^16
 * 链接：https://leetcode.cn/problems/chalkboard-xor-game/
"""

from functools import reduce
from operator import xor
from typing import List

#
# @lc app=leetcode.cn id=810 lang=python3
#
# [810] 黑板异或游戏
#


# @lc code=start
class Solution:

    def xorGame(self, nums: List[int]) -> bool:
        # 对于Alice和Bob，每次操作时，待操作的队列都有相同的奇偶性
        # n为偶数时，Alice如果不能获胜，说明对于某一位一定有奇数个1，换句话说，可擦除的数中一定包含那一位为0的数
        # 只要Alice每次选择那个数，就能保持不败（当Alice排除了所有的0之后，Bob只能移除一个1，这样会导致这个数组xor为0）
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().xorGame([163, 102, 144, 85, 111, 224, 134, 239, 212, 154, 179, 230, 203, 132, 174, 72, 122, 70, 43, 59]))
    # True
    print(Solution().xorGame([0, 1]))
    # True
    print(Solution().xorGame([1, 1, 2, 3]))
    # False
    print(Solution().xorGame([1, 1, 2]))
    # True
    print(Solution().xorGame([1, 2, 3]))
