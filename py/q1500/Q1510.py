"""
 * Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。
 * 一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。
 * 如果石子堆里没有石子了，则无法操作的玩家输掉游戏。
 * 给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/stone-game-iv/
"""

from functools import cache


class Solution:

    def winnerSquareGame1(self, n: int) -> bool:
        # 记忆化
        @cache
        def dfs(nn):
            if nn == 0: return False
            i = 1
            while i * i <= nn:
                if not dfs(nn - i * i):
                    return True
                i += 1
            return False

        return dfs(n)

    def winnerSquareGame(self, n: int) -> bool:
        # 递推
        dp = [False] * (n + 1)
        for i in range(n + 1):
            for k in range(1, i + 1):
                if k * k > i: break
                if not dp[i - k * k]:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    # True
    print(Solution().winnerSquareGame(1))
    # False
    print(Solution().winnerSquareGame(2))
    # True
    print(Solution().winnerSquareGame(4))
    # False
    print(Solution().winnerSquareGame(7))
    # False
    print(Solution().winnerSquareGame(17))