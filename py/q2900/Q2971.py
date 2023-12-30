"""
 * 给你一个长度为 n 的 正 整数数组 nums 。
 * 多边形 指的是一个至少有 3 条边的封闭二维图形。多边形的 最长边 一定 小于 所有其他边长度之和。
 * 如果你有 k （k >= 3）个 正 数 a1，a2，a3, ...，ak 满足 a1 <= a2 <= a3 <= ... <= ak 且 a1 + a2 + a3 + ... + ak-1 > ak ，
 * 那么 一定 存在一个 k 条边的多边形，每条边的长度分别为 a1 ，a2 ，a3 ， ...，ak 。
 * 一个多边形的 周长 指的是它所有边之和。
 * 请你返回从 nums 中可以构造的 多边形 的 最大周长 。如果不能构造出任何多边形，请你返回 -1 。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/
"""
from itertools import accumulate
from typing import List


class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pre_sm = [0] + list(accumulate(nums))
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] < pre_sm[i]:
                return pre_sm[i + 1]
        return -1


if __name__ == '__main__':
    # 15
    print(Solution().largestPerimeter([5, 5, 5]))
    # 12
    print(Solution().largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
    # -1
    print(Solution().largestPerimeter([5, 5, 50]))
