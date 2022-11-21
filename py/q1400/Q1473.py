"""
 * 在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不可以被重新涂色。
 * 我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）
 * 给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：
 * 1、houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
 * 2、cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
 * 请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。
 * 提示：
 * 1、m == houses.length == cost.length
 * 2、n == cost[i].length
 * 3、1 <= m <= 100
 * 4、1 <= n <= 20
 * 5、1 <= target <= m
 * 6、0 <= houses[i] <= n
 * 7、1 <= cost[i][j] <= 10^4
 * 链接：https://leetcode.cn/problems/paint-house-iii/
"""
from collections import defaultdict
from functools import cache
from typing import List


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = 0x3c3c3c3c
        ans = inf
        dp = defaultdict(lambda: defaultdict(lambda: inf))  # dp[i][j] 颜色为i、j个街区的最小花费
        dp[-1][0] = 0
        for ii, h in enumerate(houses):  # 滚动栋房子
            ndp = defaultdict(lambda: defaultdict(lambda: inf))
            if h:
                for p_i, p_dic in dp.items():
                    for p_j, p_c in p_dic.items():
                        if p_i == h - 1:
                            ndp[h - 1][p_j] = min(ndp[h - 1][p_j], p_c)
                        else:
                            ndp[h - 1][p_j + 1] = min(ndp[h - 1][p_j + 1], p_c)
            else:
                for i in range(n):  # color
                    for p_i, p_dic in dp.items():
                        for p_j, p_c in p_dic.items():
                            if p_i == i:
                                ndp[i][p_j] = min(ndp[i][p_j], p_c + cost[ii][i])
                            else:
                                ndp[i][p_j + 1] = min(ndp[i][p_j + 1], p_c + cost[ii][i])
            dp = ndp
        for i in range(n):
            ans = min(ans, dp[i][target])
        return -1 if ans == inf else ans


if __name__ == '__main__':
    # 11
    print(Solution().minCost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
    # 9
    print(Solution().minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
    # 5
    print(Solution().minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5))
    # -1
    print(Solution().minCost([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3))
