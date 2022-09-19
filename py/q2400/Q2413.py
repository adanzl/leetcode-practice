"""
 * 给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。
 * 提示：1 <= n <= 150
 * 链接：https://leetcode.cn/problems/smallest-even-multiple/
"""

from math import *


class Solution:

    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(2, n)


if __name__ == '__main__':
    # 10
    print(Solution().smallestEvenMultiple(5))
    # 6
    print(Solution().smallestEvenMultiple(6))