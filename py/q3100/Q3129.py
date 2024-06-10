"""
 * 给你 3 个正整数 zero ，one 和 limit 。
 * 一个 二进制数组 arr 如果满足以下条件，那么我们称它是 稳定的 ：
 * 1、0 在 arr 中出现次数 恰好 为 zero 。
 * 2、1 在 arr 中出现次数 恰好 为 one 。
 * 3、arr 中每个长度超过 limit 的 子数组 都 同时 包含 0 和 1 。
 * 请你返回 稳定 二进制数组的 总 数目。
 * 由于答案可能很大，将它对 10^9 + 7 取余 后返回。
 * 提示：1 <= zero, one, limit <= 200
 * 链接：https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/
"""
from functools import cache


class Solution:

    def numberOfStableArrays1(self, zero: int, one: int, limit: int) -> int:
        # 这个国服会爆内存
        MOD = 10**9 + 7
        n = zero + one

        @cache
        def func(c0, c1, lst0, lst1):
            if c0 == 0 and c1 == 0: return 1
            if c0 == 0: return 1 if n - lst0 - 1 <= limit else 0
            if c1 == 0: return 1 if n - lst1 - 1 <= limit else 0
            ret = 0
            idx = n - c0 - c1
            if c0 and idx - lst1 <= limit:
                ret += func(c0 - 1, c1, idx, lst1)

            if c1 and idx - lst0 <= limit:
                ret += func(c0, c1 - 1, lst0, idx)
            return ret % MOD

        return func(zero, one, -1, -1)

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        n = zero + one

        @cache
        def f(c0, c1, t):  # c0个0，c1个1，以b为结尾的方案数
            if c0 == 0 and c1 == 0: return 1
            if c0 == 1 and c1 == 0 and t == 0: return 1
            if c0 == 0 and c1 == 1 and t == 1: return 1
            # 前 i 个元素中有 j 个 1，且第 i 个元素填的是 t
            # f(i, j, 0) = f(i - 1, j, 0) + f(i - 1, j, 1) - f(i - l - 1, j, 1)
            # f(i, j, 1) = f(i - 1, j - 1, 0) + f(i - 1, j - 1, 1) - f(i - l - 1, j - l - 1, 0)
            if t == 0:
                if c0 <= 0: return 0
                return f(c0 - 1, c1, 0) + f(c0 - 1, c1, 1) - f(c0 - limit - 1, c1, 1)
            else:
                if c1 <= 0: return 0
                return f(c0, c1 - 1, 0) + f(c0, c1 - 1, 1) - f(c0, c1 - limit - 1, 0)

        return (f(zero, one, 0) + f(zero, one, 1)) % MOD


if __name__ == '__main__':
    # 587893473
    print(Solution().numberOfStableArrays(200, 200, 200))
    # 345095132
    print(Solution().numberOfStableArrays(55, 58, 31))
    # 1
    print(Solution().numberOfStableArrays(1, one=2, limit=1))
    # 2
    print(Solution().numberOfStableArrays(1, one=1, limit=2))
    # 14
    print(Solution().numberOfStableArrays(3, one=3, limit=2))
