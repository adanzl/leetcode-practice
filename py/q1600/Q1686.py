"""
 * Alice 和 Bob 轮流玩一个游戏，Alice 先手。
 * 一堆石子里总共有 n 个石子，轮到某个玩家时，他可以 移出 一个石子并得到这个石子的价值。
 * Alice 和 Bob 对石子价值有 不一样的的评判标准 。双方都知道对方的评判标准。
 * 给你两个长度为 n 的整数数组 aliceValues 和 bobValues 。
 * aliceValues[i] 和 bobValues[i] 分别表示 Alice 和 Bob 认为第 i 个石子的价值。
 * 所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 最优策略 进行游戏。
 * 请你推断游戏的结果，用如下的方式表示：
 * 1、如果 Alice 赢，返回 1 。
 * 2、如果 Bob 赢，返回 -1 。
 * 3、如果游戏平局，返回 0 。
 * 提示：
 * 1、n == aliceValues.length == bobValues.length
 * 2、1 <= n <= 10^5
 * 3、1 <= aliceValues[i], bobValues[i] <= 100
 * 链接：https://leetcode.cn/problems/stone-game-vi
"""

import enum
from heapq import heapify, heappop
from typing import List

#
# @lc app=leetcode.cn id=1686 lang=python3
#
# [1686] 石子游戏 VI
#


# @lc code=start
class Solution:

    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        h = [[-bobValues[i] - aliceValues[i], i] for i in range(n)]
        heapify(h)
        score = 0
        flag = 1
        while h:
            _, ii = heappop(h)
            if flag:  # alice
                score += aliceValues[ii]
            else:
                score -= bobValues[ii]
            flag ^= 1
        score = max(score, -1)
        score = min(score, 1)
        return score


# @lc code=end

if __name__ == '__main__':
    # -1
    print(Solution().stoneGameVI([2, 4, 3], bobValues=[1, 6, 7]))
    # 0
    print(Solution().stoneGameVI([1, 2], bobValues=[3, 1]))
    # 1
    print(Solution().stoneGameVI([9, 9, 5, 5, 2, 8, 2, 4, 10, 2, 3, 3, 4], [9, 5, 3, 4, 4, 6, 6, 6, 4, 3, 7, 5, 10]))
    # 1
    print(Solution().stoneGameVI([1, 3], bobValues=[2, 1]))
