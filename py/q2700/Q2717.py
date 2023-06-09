"""
 * 给你一个下标从 0 开始、长度为 n 的整数排列 nums 。
 * 如果排列的第一个数字等于 1 且最后一个数字等于 n ，则称其为 半有序排列 。你可以执行多次下述操作，直到将 nums 变成一个 半有序排列 ：
 * 选择 nums 中相邻的两个元素，然后交换它们。
 * 返回使 nums 变成 半有序排列 所需的最小操作次数。
 * 排列 是一个长度为 n 的整数序列，其中包含从 1 到 n 的每个数字恰好一次。
 * 提示：
 * 1、2 <= nums.length == n <= 50
 * 2、1 <= nums[i] <= 50
 * 3、nums 是一个 排列
 * 链接：https://leetcode.cn/problems/semi-ordered-permutation/
"""
from typing import List


class Solution:

    def semiOrderedPermutation(self, nums: List[int]) -> int:
        i0, i1 = 0, 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 1: i0 = i
            if num == n: i1 = i
        return i0 + n - i1 - 1 - (1 if i0 > i1 else 0)


if __name__ == '__main__':
    # 2
    print(Solution().semiOrderedPermutation([2, 1, 4, 3]))
    # 3
    print(Solution().semiOrderedPermutation([2, 4, 1, 3]))
    # 0
    print(Solution().semiOrderedPermutation([1, 3, 4, 2, 5]))
