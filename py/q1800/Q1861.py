"""
 * 给你一个 m x n 的字符矩阵 box ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
 * 1、'#' 表示石头
 * 2、'*' 表示固定的障碍物
 * 3、'.' 表示空位置
 * 这个箱子被 顺时针旋转 90 度 ，由于重力原因，部分石头的位置会发生改变。
 * 每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。
 * 重力 不会 影响障碍物的位置，同时箱子旋转不会产生惯性 ，也就是说石头的水平位置不会发生改变。
 * 题目保证初始时 box 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。
 * 请你返回一个 n x m的矩阵，表示按照上述旋转后，箱子内的结果。
 * 提示：
 * 1、m == box.length
 * 2、n == box[i].length
 * 3、1 <= m, n <= 500
 * 4、box[i][j] 只可能是 '#' ，'*' 或者 '.' 。
 * 链接：https://leetcode.cn/problems/rotating-the-box/
"""
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, reduce
from heapq import (heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest)
from itertools import (accumulate, chain, combinations, combinations_with_replacement, count, cycle, groupby, pairwise,
                       permutations, product, repeat, zip_longest)
from math import comb, factorial, gcd, inf, isqrt, lcm, log2
from operator import and_, iconcat, mul, or_, xor
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [['.'] * m for _ in range(n)]
        for i in range(m):
            p = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':  # 障碍物
                    p = j - 1
                    ans[j][m - 1 - i] = box[i][j]
                elif box[i][j] == '.':  # 空位置
                    p = max(p, j)
                    ans[j][m - 1 - i] = '.'
                else:  # 石头
                    ans[j][m - 1 - i] = '.'
                    ans[p][m - 1 - i] = '#'
                    p -= 1
        return ans


if __name__ == '__main__':
    # [["."], ["#"], ["#"]]
    print(Solution().rotateTheBox([["#", ".", "#"]]))
    # [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]
    print(Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]))
    # [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]]
    print(Solution().rotateTheBox([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."],
                                   ["#", "#", "#", ".", "#", "."]]))
