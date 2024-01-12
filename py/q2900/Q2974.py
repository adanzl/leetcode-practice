"""
 * 你有一个下标从 0 开始、长度为 偶数 的整数数组 nums ，同时还有一个空数组 arr 。
 * Alice 和 Bob 决定玩一个游戏，游戏中每一轮 Alice 和 Bob 都会各自执行一次操作。游戏规则如下：
 * 1、每一轮，Alice 先从 nums 中移除一个 最小 元素，然后 Bob 执行同样的操作。
 * 2、接着，Bob 会将移除的元素添加到数组 arr 中，然后 Alice 也执行同样的操作。
 * 3、游戏持续进行，直到 nums 变为空。
 * 返回结果数组 arr 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、nums.length % 2 == 0
 * 链接：https://leetcode.cn/problems/minimum-number-game/
"""
from typing import List


class Solution:

    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == '__main__':
    # [3, 2, 5, 4]
    print(Solution().numberGame([5, 4, 2, 3]))
    # [5, 2]
    print(Solution().numberGame([2, 5]))
