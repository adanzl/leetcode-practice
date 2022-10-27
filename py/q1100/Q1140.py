"""
 * 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
 * 爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
 * 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
 * 游戏一直持续到所有石子都被拿走。
 * 假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。
 * 提示：
 * 1、1 <= piles.length <= 100
 * 2、1 <= piles[i] <= 10^4
 * 链接：https://leetcode.cn/problems/stone-game-ii/
"""
from functools import cache
from itertools import accumulate
from typing import List


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre_sum = [0] + list(accumulate(piles))

        @cache
        def f(idx, M):
            remain = n - idx
            if remain <= M * 2:
                return pre_sum[n] - pre_sum[idx]
            ans = 0
            for i in range(1, min(M * 2, remain) + 1):
                ans = max(ans, pre_sum[i + idx] - pre_sum[idx] + pre_sum[-1] - pre_sum[idx + i] - f(idx + i, max(M, i)))
            return ans

        return f(0, 1)


if __name__ == '__main__':
    # 10
    print(Solution().stoneGameII([2, 7, 9, 4, 4]))
    # 104
    print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))
