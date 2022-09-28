from functools import *
"""
 * 有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
 * 给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10^9 + 7 取模 的值。
 * 平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/domino-and-tromino-tiling
"""


class Solution:

    def numTilings(self, n: int) -> int:
        MOD = int(1e9 + 7)
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0] = [1, 0, 0]
        for i in range(0, n + 1):
            if i + 1 <= n:
                dp[i + 1][0] = (dp[i + 1][0] + dp[i][0] + dp[i][1] + dp[i][2]) % MOD
                dp[i + 1][1] = (dp[i + 1][1] + dp[i][2]) % MOD
                dp[i + 1][2] = (dp[i + 1][2] + dp[i][1]) % MOD
            if i + 2 <= n:
                dp[i + 2][0] = (dp[i + 2][0] + dp[i][0]) % MOD
                dp[i + 2][1] = (dp[i + 2][1] + dp[i][0]) % MOD
                dp[i + 2][2] = (dp[i + 2][2] + dp[i][0]) % MOD

        return dp[n][0]


if __name__ == '__main__':
    # 5
    print(Solution().numTilings(3))
    # 1
    print(Solution().numTilings(1))
    # 979232805
    print(Solution().numTilings(1000))
    # 190242381
    print(Solution().numTilings(100))
    # 1255
    print(Solution().numTilings(10))