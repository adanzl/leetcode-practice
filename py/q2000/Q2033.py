"""
 * 给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。
 * 单值网格 是全部元素都相等的网格。
 * 返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 10^5
 * 5、1 <= x, grid[i][j] <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-a-uni-value-grid
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

#
# @lc app=leetcode.cn id=2033 lang=python3
# @lcpr version=30104
#
# [2033] 获取单值网格的最小操作数
#

# @lc code=start
INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        r = None
        arr = []
        for row in grid:
            for v in row:
                if r is None:
                    r = v % x
                else:
                    if (v - r) % x != 0:
                        return -1
                arr.append(v)
        arr.sort()
        n = len(arr)
        if n == 1: return 0
        v1, v2 = 0, 0
        t1, t2 = arr[n // 2 - 1], arr[n // 2]
        i1, i2 = n // 2 - 1, n // 2
        if n % 2 == 0:
            i2 =  i1
            t2 = t1
        for i in range(n):
            if i < i1:
                v1 += (t1 - arr[i]) // x
            else:
                v1 += (arr[i] - t1) // x
            if i < i2:
                v2 += (t2 - arr[i]) // x
            else:
                v2 += (arr[i] - t2) // x
        return min(v1, v2)


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().minOperations([[2, 4], [6, 8]], x=2))
    # 5
    print(Solution().minOperations([[1, 5], [2, 3]], x=1))
    # -1
    print(Solution().minOperations([[1, 2], [3, 4]], x=2))
