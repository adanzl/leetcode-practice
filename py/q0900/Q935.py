"""
 * 象棋骑士有一个独特的移动方式，它可以垂直移动两个方格，水平移动一个方格，或者水平移动两个方格，垂直移动一个方格(两者都形成一个 L 的形状)。
 * 象棋骑士可能的移动方式如下图所示:
 * 我们有一个象棋骑士和一个电话垫，如下所示，骑士只能站在一个数字单元格上(即蓝色单元格)。
 * 给定一个整数 n，返回我们可以拨多少个长度为 n 的不同电话号码。
 * 你可以将骑士放置在任何数字单元格上，然后你应该执行 n - 1 次移动来获得长度为 n 的号码。所有的跳跃应该是有效的骑士跳跃。
 * 因为答案可能很大，所以输出答案模 10^9 + 7.
 * 提示：1 <= n <= 5000
 * 链接：https://leetcode.cn/problems/knight-dialer/
"""
from typing import *


class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * 10
        for i in range(n - 1):
            dp = [dp[4] + dp[6], dp[6] + dp[8], dp[7] + dp[9], dp[4] + dp[8], dp[0] + dp[3] + dp[9], 0, dp[1] + dp[7] + dp[0], dp[2] + dp[6], dp[1] + dp[3], dp[2] + dp[4]]
        return sum(dp) % MOD


if __name__ == '__main__':
    # 10
    print(Solution().knightDialer(1))
    # 20
    print(Solution().knightDialer(2))
    # 136006598
    print(Solution().knightDialer(3131))
    # 406880451
    print(Solution().knightDialer(5000))