"""
 * 给你一个下标从 0 开始且长度为 n 的整数数组 differences ，它表示一个长度为 n + 1 的 隐藏 数组 相邻 元素之间的 差值 。
 * 更正式的表述为：我们将隐藏数组记作 hidden ，那么 differences[i] = hidden[i + 1] - hidden[i] 。
 * 同时给你两个整数 lower 和 upper ，它们表示隐藏数组中所有数字的值都在 闭 区间 [lower, upper] 之间。
 * 比方说，differences = [1, -3, 4] ，lower = 1 ，upper = 6 ，
 * 那么隐藏数组是一个长度为 4 且所有值都在 1 和 6 （包含两者）之间的数组。
 * 1、[3, 4, 1, 5] 和 [4, 5, 2, 6] 都是符合要求的隐藏数组。
 * 2、[5, 6, 3, 7] 不符合要求，因为它包含大于 6 的元素。
 * 3、[1, 2, 3, 4] 不符合要求，因为相邻元素的差值不符合给定数据。
 * 请你返回 符合 要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 0 。
 * 提示：
 * 1、n == differences.length
 * 2、1 <= n <= 10^5
 * 3、-10^5 <= differences[i] <= 10^5
 * 4、-10^5 <= lower <= upper <= 10^5
 * 链接：https://leetcode.cn/problems/count-the-hidden-sequences/
"""

from typing import List

#
# @lc app=leetcode.cn id=2145 lang=python3
#
# [2145] 统计隐藏数组数目
#


# @lc code=start
class Solution:

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        arr = [0]
        for d in differences:
            arr.append(arr[-1] + d)
        mx, mn = max(arr), min(arr)
        ans = upper - (mx + lower - mn) + 1
        return max(ans, 0)


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().numberOfArrays([4, -7, 2], lower=3, upper=6))
    # 4
    print(Solution().numberOfArrays([3, -4, 5, 1, -2], lower=-4, upper=5))
    # 2
    print(Solution().numberOfArrays([1, -3, 4], lower=1, upper=6))
