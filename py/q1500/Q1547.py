"""
 * 有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：
 * 给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。
 * 你可以按顺序完成切割，也可以根据需要更改切割的顺序。
 * 每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。
 * 返回切棍子的 最小总成本 。
 * 提示：
 * 1、2 <= n <= 10^6
 * 2、1 <= cuts.length <= min(n - 1, 100)
 * 3、1 <= cuts[i] <= n - 1
 * 4、cuts 数组中的所有整数都 互不相同
 * 链接：https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/
"""
from functools import cache
from typing import List


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        # 记忆化 加两刀
        nc = len(cuts)
        cuts.sort()

        @cache
        def dfs(l, r):
            if r - l == 1: return 0
            ret = 0x3c3c3c3c
            up, down = cuts[r - 1] if r < nc + 1 else n, cuts[l - 1] if l else 0
            for i in range(l + 1, r):
                ret = min(ret, dfs(l, i) + dfs(i, r))
            return ret + up - down

        return dfs(0, nc + 1)


if __name__ == '__main__':
    # 22
    print(Solution().minCost(9, [5, 6, 1, 4, 2]))
    # 16
    print(Solution().minCost(7, [1, 3, 4, 5]))