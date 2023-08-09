"""
 * 给你两个 正 整数 n 和 x 。
 * 请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。
 * 换句话说，你需要返回互不相同整数 [n1, n2, ..., nk] 的集合数目，满足 n = n1^x + n2^x + ... + nk^x 。
 * 由于答案可能非常大，请你将它对 10^9 + 7 取余后返回。
 * 比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 2^3 + 3^3 + 5^3 。
 * 提示：
 * 1、1 <= n <= 300
 * 2、1 <= x <= 5
 * 链接：https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/
"""

from itertools import count

MX_N, MX_X = 300, 5
ans = [[1] + [0] * MX_N for _ in range(MX_X + 1)]  # x-n
for x in range(1, MX_X + 1):
    for i in count(1):
        v = i**x
        if v > MX_N: break
        for s in range(MX_N, v - 1, -1):
            ans[x][s] += ans[x][s - v]


class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        return ans[x][n] % (10**9 + 7)


if __name__ == '__main__':
    # 872765252
    print(Solution().numberOfWays(297, 1))
    # 1
    print(Solution().numberOfWays(10, x=2))
    # 2
    print(Solution().numberOfWays(4, x=1))
