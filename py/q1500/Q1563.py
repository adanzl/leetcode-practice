"""
 * 几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
 * 游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）;Bob 负责计算每一行的值，即此行中所有石子的值的总和。
 * Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。
 * 只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
 * 返回 Alice 能够获得的最大分数 。
 * 提示：
 * 1、1 <= stoneValue.length <= 500
 * 2、1 <= stoneValue[i] <= 10^6
 * 链接：https://leetcode.cn/problems/stone-game-v/
"""
import sys

sys.setrecursionlimit(5 * 10**5)
from bisect import bisect_left
from functools import cache
from itertools import accumulate
from typing import List


class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:
        pre_sum = [0] + list(accumulate(stoneValue))

        @cache
        def dfs(i, j):
            if i >= j: return 0
            ans = 0
            half = (pre_sum[j + 1] + pre_sum[i]) / 2
            # 使用二分查找左右的大小中心位置
            idx = bisect_left(pre_sum, half, lo=i, hi=j + 1)
            # idx 左边, left更小; idx 右边, right更小
            if pre_sum[idx] == half:
                ans = max(ans, left_dfs(i, idx), right_dfs(idx, j))
            else:
                ans = max(ans, left_dfs(i, idx - 1))
                ans = max(ans, right_dfs(idx, j))
            return ans

        @cache
        def left_dfs(i, j):
            if i >= j: return 0
            return max(pre_sum[j] - pre_sum[i] + dfs(i, j - 1), left_dfs(i, j - 1))

        @cache
        def right_dfs(i, j):
            if i >= j + 1: return 0
            return max(pre_sum[j + 1] - pre_sum[i] + dfs(i, j), right_dfs(i + 1, j))

        return dfs(0, len(stoneValue) - 1)


if __name__ == '__main__':
    # 18
    print(Solution().stoneGameV([6, 2, 3, 4, 5, 5]))
    # 28
    print(Solution().stoneGameV([7, 7, 7, 7, 7, 7, 7]))
    # 0
    print(Solution().stoneGameV([4]))