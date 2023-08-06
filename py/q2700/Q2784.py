"""
 * 给你一个整数数组 nums ，如果它是数组 base[n] 的一个排列，我们称它是个 好 数组。
 * base[n] = [1, 2, ..., n - 1, n, n] （换句话说，它是一个长度为 n + 1 且包含 1 到 n - 1 恰好各一次，
 * 包含 n  两次的一个数组）。比方说，base[1] = [1, 1] ，base[3] = [1, 2, 3, 3] 。
 * 如果数组是一个好数组，请你返回 true ，否则返回 false 。
 * 注意：数组的排列是这些数字按任意顺序排布后重新得到的数组。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= num[i] <= 200
 * 链接：https://leetcode.cn/problems/check-if-array-is-good/
"""
from typing import List


class Solution:

    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if i != nums[i] - 1:
                return False
        return nums[-1] == len(nums) - 1


if __name__ == '__main__':
    # False
    print(Solution().isGood([1]))
    # True
    print(Solution().isGood([1, 1]))
    # False
    print(Solution().isGood([2, 1, 3]))
    # True
    print(Solution().isGood([1, 3, 3, 2]))
    # False
    print(Solution().isGood([3, 4, 4, 1, 2, 1]))