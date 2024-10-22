"""
 * 给你三个整数 n ，x 和 y 。
 * 一个活动总共有 n 位表演者。每一位表演者会 被安排 到 x 个节目之一，有可能有节目 没有 任何表演者。
 * 所有节目都安排完毕后，评委会给每一个 有表演者的 节目打分，分数是一个 [1, y] 之间的整数。
 * 请你返回 总 的活动方案数。
 * 答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 注意 ，如果两个活动满足以下条件 之一 ，那么它们被视为 不同 的活动：
 * 1、存在 一个表演者在不同的节目中表演。
 * 2、存在 一个节目的分数不同。
 * 提示：1 <= n, x, y <= 1000
 * 链接：https://leetcode.cn/problems/find-the-number-of-possible-ways-for-an-event/
"""
from functools import cache
import math

INF = 0x3c3c3c3c3c3c3c3c3c

MOD = 1_000_000_007
MX = 1001

# 第二类斯特林数
stl2 = [[0] * MX for _ in range(MX)]
stl2[0][0] = 1
for i in range(1, MX):
    for j in range(1, i + 1):
        stl2[i][j] = (stl2[i - 1][j - 1] + j * stl2[i - 1][j]) % MOD


@cache
def stirling2(n, k):
    if n == k == 0:
        return 1
    if n > 0 and k == 0:
        return 0
    if n == k:
        return 1
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def permutation(n, k):  # A(n, k)
    return math.factorial(n) // math.factorial(n - k)


class Solution:

    def numberOfWays(self, n: int, x: int, y: int) -> int:
        ans = 0

        perm = pow_y = 1
        for ii in range(1, min(x, n) + 1):
            # x 个节目中选出 ii 个节目 等待分配 有顺序
            # n 个人分配到 ii 个任务中，无顺序 第二类斯特林数
            perm = perm * (x + 1 - ii) % MOD
            pow_y = pow_y * y % MOD
            ans += pow_y * perm * stl2[n][ii]
            # ans += pow_y * stirling2(n, ii) * permutation(x, ii)
        return ans % MOD


if __name__ == '__main__':
    # 544840908
    print(Solution().numberOfWays(76, 31, 194))
    # 6
    print(Solution().numberOfWays(1, x=2, y=3))
    # 32
    print(Solution().numberOfWays(5, x=2, y=1))
    # 684
    print(Solution().numberOfWays(3, x=3, y=4))
