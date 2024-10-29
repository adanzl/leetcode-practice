"""
 * 给你两个整数 n 和 k ，和两个二维整数数组 stayScore 和 travelScore 。
 * 一位旅客正在一个有 n 座城市的国家旅游，每座城市都 直接 与其他所有城市相连。这位游客会旅游 恰好 k 天（下标从 0 开始），且旅客可以选择 任意 城市作为起点。
 * 每一天，这位旅客都有两个选择：
 * 1、留在当前城市：如果旅客在第 i 天停留在前一天所在的城市 cur ，旅客会获得 stayScore[i][crr] 点数。
 * 2、前往另外一座城市：如果旅客从城市 cur 前往城市 dest ，旅客会获得 travelScore[cur][dest] 点数。
 * 请你返回这位旅客可以获得的 最多 点数。
 * 提示：
 * 1、1 <= n <= 200
 * 2、1 <= k <= 200
 * 3、n == travelScore.length == travelScore[i].length == stayScore[i].length
 * 4、k == stayScore.length
 * 5、1 <= stayScore[i][j] <= 100
 * 6、0 <= travelScore[i][j] <= 100
 * 7、travelScore[i][i] == 0
 * 链接：https://leetcode.cn/problems/maximum-points-tourist-can-earn/
"""
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

    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def dfs(c_i, kk):
            if kk == 0: return 0
            ret = dfs(c_i, kk - 1) + stayScore[k - kk][c_i]  # stay
            for i in range(n):
                if i == c_i: continue
                ret = max(ret, dfs(i, kk - 1) + travelScore[c_i][i])
            return ret

        return max(dfs(i, k) for i in range(n))


if __name__ == '__main__':
    # 3
    print(Solution().maxScore(2, k=1, stayScore=[[2, 3]], travelScore=[[0, 2], [1, 0]]))
    # 8
    print(Solution().maxScore(3, k=2, stayScore=[[3, 4, 2], [2, 1, 2]], travelScore=[[0, 2, 1], [2, 0, 4], [3, 2, 0]]))
    #
    # print(Solution().maxScore())
