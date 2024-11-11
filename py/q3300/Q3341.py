"""
 * 有一个地窖，地窖中有 n x m 个房间，它们呈网格状排布。
 * 给你一个大小为 n x m 的二维数组 moveTime ，其中 moveTime[i][j] 表示在这个时刻 以后 你才可以 开始 往这个房间 移动 。
 * 你在时刻 t = 0 时从房间 (0, 0) 出发，每次可以移动到 相邻 的一个房间。在 相邻 房间之间移动需要的时间为 1 秒。
 * 请你返回到达房间 (n - 1, m - 1) 所需要的 最少 时间。
 * 如果两个房间有一条公共边（可以是水平的也可以是竖直的），那么我们称这两个房间是 相邻 的。
 * 提示：
 * 1、2 <= n == moveTime.length <= 50
 * 2、2 <= m == moveTime[i].length <= 50
 * 3、0 <= moveTime[i][j] <= 10^9
 * 链接：https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-i/
"""
from multiprocessing import heap
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, \
    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        f = [[INF] * n for _ in range(m)]
        f[0][0] = 0
        q = [(0, 0, 0)]
        heapify(q)
        vis = set()
        while q:
            vv, x, y = heappop(q)
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if f[nx][ny] >= vv + 1:
                    if vv + 1 > moveTime[nx][ny]:
                        f[nx][ny] = vv + 1
                    else:
                        f[nx][ny] = moveTime[nx][ny] + 1
                    val = (f[nx][ny], nx, ny)
                    if val not in vis:
                        vis.add(val)
                        heappush(q, val)
        return f[-1][-1]


if __name__ == '__main__':
    # 6
    print(Solution().minTimeToReach([[0, 4], [4, 4]]))
    # 3
    print(Solution().minTimeToReach([[0, 0, 0], [0, 0, 0]]))
    # 3
    print(Solution().minTimeToReach([[0, 1], [1, 2]]))
