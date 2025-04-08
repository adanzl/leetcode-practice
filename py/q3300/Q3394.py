"""
 * 给你一个整数 n 表示一个 n x n 的网格图，坐标原点是这个网格图的左下角。同时给你一个二维坐标数组 rectangles ，
 * 其中 rectangles[i] 的格式为 [start_x, start_y, end_x, end_y] ，表示网格图中的一个矩形。每个矩形定义如下：
 * 1、(start_x, start_y)：矩形的左下角。
 * 2、(end_x, end_y)：矩形的右上角。
 * 注意 ，矩形相互之间不会重叠。你的任务是判断是否能找到两条 要么都垂直要么都水平 的 两条切割线 ，满足：
 * 1、切割得到的三个部分分别都 至少 包含一个矩形。
 * 2、每个矩形都 恰好仅 属于一个切割得到的部分。
 * 如果可以得到这样的切割，请你返回 true ，否则返回 false 。
 * 提示：
 * 1、3 <= n <= 10^9
 * 2、3 <= rectangles.length <= 10^5
 * 3、0 <= rectangles[i][0] < rectangles[i][2] <= n
 * 4、0 <= rectangles[i][1] < rectangles[i][3] <= n
 * 5、矩形之间两两不会有重叠。
 * 链接：https://leetcode.cn/problems/check-if-grid-can-be-cut-into-sections
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

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = []
        y = []
        for s_x, s_y, e_x, e_y in rectangles:
            x.append([s_x, -e_x])
            y.append([s_y, -e_y])

        def check(arr):
            arr.sort()
            p = 0
            cnt = 0
            for l, r in arr:
                if l < p:
                    p = max(p, -r)
                else:
                    if p > 0:
                        cnt += 1
                    p = -r
            return cnt >= 2

        return check(y) or check(x)


if __name__ == '__main__':
    # True
    print(Solution().checkValidCuts(5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
    # True
    print(Solution().checkValidCuts(4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
    # False
    print(Solution().checkValidCuts(4,
                                    rectangles=[[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))
