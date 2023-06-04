"""
 * 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：
 * 1、num1 <= x <= num2
 * 2、min_sum <= digit_sum(x) <= max_sum.
 * 请你返回好整数的数目。答案可能很大，请返回答案对 10^9 + 7 取余后的结果。
 * 注意，digit_sum(x) 表示 x 各位数字之和。
 * 提示：
 * 1、1 <= num1 <= num2 <= 10^22
 * 2、1 <= min_sum <= max_sum <= 400
 * 链接：https://leetcode.cn/problems/count-of-integers/
"""
from functools import cache


class Solution:

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        n = len(num2)
        l_n1, l_n2 = ["0"] * (n - len(num1)) + list(num1), list(num2)

        @cache
        def func(limit_l, limit_r, idx, mn, mx):
            if mx < 0: return 0
            if idx == n:
                return 1 if mn <= 0 <= mx else 0
            ans = 0
            l = int(l_n1[idx]) if limit_l else 0
            r = int(l_n2[idx]) if limit_r else 9
            for v in range(l, r + 1):
                ans = (ans + func(str(v) == l_n1[idx] and limit_l, str(v) == l_n2[idx] and limit_r, idx + 1, mn - v, mx - v)) % MOD
            return ans

        return func(True, True, 0, min_sum, max_sum)


if __name__ == '__main__':
    # 45
    print(Solution().count("1", str(10**2), 1, 8))
    # 11
    print(Solution().count("1", "12", 1, 8))
    # 5
    print(Solution().count("1", "5", 1, 5))
    # 490000
    print(Solution().count("1", str(10**22), 1, 400))