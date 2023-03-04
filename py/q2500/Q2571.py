"""
 * 给你一个正整数 n ，你可以执行下述操作 任意 次：
 * n 加上或减去 2 的某个 幂
 * 返回使 n 等于 0 需要执行的 最少 操作数。
 * 如果 x == 2^i 且其中 i >= 0 ，则数字 x 是 2 的幂。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0/
"""

from functools import cache


class Solution:

    def minOperations(self, n: int) -> int:

        @cache
        def func(n):
            if n == 0: return 0
            if n == 1: return 1
            if n & 1: return min(func(n >> 1), func((n + 1) >> 1)) + 1
            return func(n >> 1)

        return func(n)


if __name__ == '__main__':
    # 3
    print(Solution().minOperations(39))
    # 3
    print(Solution().minOperations(54))