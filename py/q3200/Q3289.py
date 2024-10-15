"""
 * 数字小镇 DigitVillage 中，存在一个数字列表 nums，其中包含从 0 到 n - 1 的整数。
 * 每个数字本应 只出现一次，然而，有 两个 顽皮的数字额外多出现了一次，使得列表变得比正常情况下更长。
 * 为了恢复 DigitVillage 的和平，作为小镇中的名侦探，请你找出这两个顽皮的数字。
 * 返回一个长度为 2 的数组，包含这两个数字（顺序任意）。
 * 提示：
 * 1、2 <= n <= 100
 * 2、nums.length == n + 2
 * 3、0 <= nums[i] < n
 * 4、输入保证 nums 中 恰好 包含两个重复的元素。
 * 链接：https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville/
"""
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [v for v, c in Counter(nums).items() if 2 == c]


if __name__ == '__main__':
    # [0,1]
    print(Solution().getSneakyNumbers([0, 1, 1, 0]))
    # [2,3]
    print(Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2]))
    # [4,5]
    print(Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
