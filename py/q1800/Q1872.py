"""
 * Alice 和 Bob 玩一个游戏，两人轮流操作， Alice 先手 。
 * 总共有 n 个石子排成一行。轮到某个玩家的回合时，如果石子的数目 大于 1 ，他将执行以下操作：
 * 1、选择一个整数 x > 1 ，并且 移除 最左边的 x 个石子。
 * 2、将 移除 的石子价值之 和 累加到该玩家的分数中。
 * 3、将一个 新的石子 放在最左边，且新石子的值为被移除石子值之和。
 * 当只剩下 一个 石子时，游戏结束。
 * Alice 和 Bob 的 分数之差 为 (Alice 的分数 - Bob 的分数) 。 Alice 的目标是 最大化 分数差，Bob 的目标是 最小化 分数差。
 * 给你一个长度为 n 的整数数组 stones ，其中 stones[i] 是 从左边起 第 i 个石子的价值。请你返回在双方都采用 最优 策略的情况下，Alice 和 Bob 的 分数之差 。
 * 提示：
 * 1、n == stones.length
 * 2、2 <= n <= 10^5
 * 3、-10^4 <= stones[i] <= 10^4
 * 链接：https://leetcode.cn/problems/stone-game-viii/
"""
from itertools import accumulate
from typing import List


class Solution:

    def stoneGameVIII(self, stones: List[int]) -> int:
        pre_sum = list(accumulate(stones))
        # 题目转换为两人在pre_sum中选择数字，求最大差值
        # dp[i]表示 [1, n) 中，Alice获得的最大差值，可以根据Alice是否选择 pre_sum[i] 来分为两种情况
        # 1、Alice选择 pre_sum[i] 时，Bob 获得 dp[i+1]，Alice获得 pre_sum[i] - dp[i+1]
        # 2、Alice不选择 pre_sum[i] 时，Alice获得 dp[i+1]
        # 以上两种情况选最大值
        n = len(stones)
        dp = [0] * (n)
        dp[-1] = pre_sum[-1]
        for i in range(n - 2, 0, -1):
            dp[i] = max(pre_sum[i] - dp[i + 1], dp[i + 1])
        return dp[1]


if __name__ == '__main__':
    # 5
    print(Solution().stoneGameVIII([-1, 2, -3, 4, -5]))
    # 13
    print(Solution().stoneGameVIII([7, -6, 5, 10, 5, -2, -6]))
    # -22
    print(Solution().stoneGameVIII([-10, -12]))
