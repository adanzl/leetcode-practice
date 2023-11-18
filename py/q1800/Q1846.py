"""
 * 给你一个正整数数组 arr 。请你对 arr 执行一些操作（也可以不进行任何操作），使得数组满足以下条件：
 * 1、arr 中 第一个 元素必须为 1 。
 * 2、任意相邻两个元素的差的绝对值 小于等于 1 ，也就是说，对于任意的 1 <= i < arr.length （数组下标从 0 开始），
 *      都满足 abs(arr[i] - arr[i - 1]) <= 1 。abs(x) 为 x 的绝对值。
 * 你可以执行以下 2 种操作任意次：
 * 1、减小 arr 中任意元素的值，使其变为一个 更小的正整数 。
 * 2、重新排列 arr 中的元素，你可以以任意顺序重新排列。
 * 请你返回执行以上操作后，在满足前文所述的条件下，arr 中可能的 最大值 。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-element-after-decreasing-and-rearranging
"""

from typing import List

#
# @lc app=leetcode.cn id=1846 lang=python3
#
# [1846] 减小和重新排列数组后的最大元素
#


# @lc code=start
class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n):
            ans = min(i + 1, arr[i], ans + 1)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))
    # 3
    print(Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]))
    # 5
    print(Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]))
