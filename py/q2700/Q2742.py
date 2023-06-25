"""
 * 给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：
 * 1、一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，开销为 cost[i] 单位的钱。
 * 2、一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
 * 请你返回刷完 n 堵墙最少开销为多少。
 * 提示：
 * 1、1 <= cost.length <= 500
 * 2、cost.length == time.length
 * 3、1 <= cost[i] <= 10^6
 * 4、1 <= time[i] <= 500
 * 链接：https://leetcode.cn/problems/painting-the-walls/
"""
from functools import cache
from typing import List


class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        INF = 10**10
        n = len(cost)

        @cache
        def dfs(idx, d):  # 前idx组数据，付费工作时间与免费工作时间的差为d，返回最小开销
            if d > idx: return 0
            if idx == -1: return INF
            return min(dfs(idx - 1, d + time[idx]) + cost[idx], dfs(idx - 1, d - 1))  # 第idx组数据是否为免费数据

        return dfs(n - 1, 0)


if __name__ == '__main__':
    # 62
    print(Solution().paintWalls([49, 35, 32, 20, 30, 12, 42], [1, 1, 2, 2, 1, 1, 2]))
    # 4
    print(Solution().paintWalls([2, 3, 4, 2], time=[1, 1, 1, 1]))
    # 12
    print(Solution().paintWalls([8, 7, 5, 15], [1, 1, 2, 1]))
    # 3
    print(Solution().paintWalls([1, 2, 3, 2], time=[1, 2, 3, 2]))
