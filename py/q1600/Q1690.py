"""
 * 石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。
 * 有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。
 * 当没有石头可移除时，得分较高者获胜。
 * 鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。
 * 爱丽丝的目标是最大限度地 扩大得分的差值 。
 * 给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，
 * 如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分的差值 。
 * 提示：
 * 1、n == stones.length
 * 2、2 <= n <= 1000
 * 3、1 <= stones[i] <= 1000
 * 链接：https://leetcode.cn/problems/stone-game-vii
"""
from functools import cache
from itertools import accumulate
from typing import List


class Solution:

    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pre_sum = [0] + list(accumulate(stones))

        @cache
        def func(l, r):  # return 先手得分,后手得分
            if l == r: return 0, 0
            sl = pre_sum[r + 1] - pre_sum[l + 1]
            sr = pre_sum[r] - pre_sum[l]
            ret_l, ret_r = func(l + 1, r), func(l, r - 1)
            score_l = ret_l[1] + sl, ret_l[0]
            score_r = ret_r[1] + sr, ret_r[0]
            if score_l[0] - score_l[1] < score_r[0] - score_r[1]:
                score_l, score_r = score_r, score_l
            return score_l

        sa, sb = func(0, n - 1)
        func.cache_clear()
        return sa - sb


if __name__ == '__main__':
    # 6
    print(Solution().stoneGameVII([5, 3, 1, 4, 2]))
    # 122
    print(Solution().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))
    #
    # print(Solution().stoneGameVII())
