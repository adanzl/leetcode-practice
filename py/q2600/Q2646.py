"""
 * 现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。
 * 给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。
 * 每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。
 * 给定路径的 价格总和 是该路径上所有节点的价格之和。
 * 另给你一个二维整数数组 trips ，其中 trips[i] = [start_i, end_i] 表示您从节点 start_i 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 end_i 。
 * 在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。
 * 返回执行所有旅行的最小价格总和。
 * 提示：
 * 1、1 <= n <= 50
 * 2、edges.length == n - 1
 * 3、0 <= ai, bi <= n - 1
 * 4、edges 表示一棵有效的树
 * 5、price.length == n
 * 6、price[i] 是一个偶数
 * 7、1 <= price[i] <= 1000
 * 8、1 <= trips.length <= 100
 * 9、0 <= start_i, end_i <= n - 1
 * 链接：https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
"""
from collections import Counter
from functools import cache
from typing import List


class Solution:

    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ways_cnt = Counter()
        ways = [[[i] for i in range(n)] for __ in range(n)]

        def build_way(s, e, fa):
            for nx in g[e]:
                if nx == fa: continue
                ways[s][nx] = ways[nx][s] = ways[s][e][:] + [nx]
                build_way(s, nx, e)

        for i in range(n):
            build_way(i, i, i)
        for u, v in trips:
            way = ways[u][v]
            for c in way:
                ways_cnt[c] += 1

        @cache
        def func(idx, fa, half):
            p = price[idx] // 2 if half else price[idx]
            ret = p * ways_cnt[idx]
            for nx in g[idx]:
                if nx == fa: continue
                if half:
                    ret += func(nx, idx, False)
                else:
                    ret += min(func(nx, idx, False), func(nx, idx, True))
            return ret

        return min(func(0, -1, False), func(0, -1, True))


if __name__ == '__main__':
    # 44881
    print(Solution().minimumTotalPrice(n=48,
                                       edges=[[1, 40], [5, 13], [10, 23], [14, 13], [19, 16], [20, 3], [21, 4], [4, 42], [22, 18], [24, 12], [26, 13], [13, 42], [27, 32], [29, 25], [25, 30], [30, 23],
                                              [31, 6], [6, 23], [23, 12], [12, 18], [18, 43], [33, 28], [36, 7], [37, 2], [2, 35], [35, 42], [39, 41], [40, 32], [41, 34], [42, 38], [38, 47], [44, 43],
                                              [43, 0], [0, 16], [16, 28], [28, 11], [11, 46], [45, 15], [46, 34], [34, 32], [32, 3], [3, 7], [7, 8], [8, 15], [15, 9], [9, 17], [17, 47]],
                                       price=[134,52,60,56,80,92,28,118,26,28,68,108,90,94,10,24,10,4,92,66,64,114,86,38,130,4,50,72,18,66,118,128,126,18,34,104,108,34,80,82,132,122,116,8,146,8,32,102],
                                       trips=[[19,0],[41,39],[24,46],[5,43],[46,25],[42,6],[10,26],[18,12],[44,41],[20,28],[35,9],[31,4],[18,11],[26,40],[28,40],[43,38],[33,20],[23,7],[31,31],[15,0],[44,33],[38,37],[30,20],[8,13],[4,10],[37,25],[3,19],[43,29],[1,34],[29,25],[14,25],[9,9],[20,43],[7,22],[6,36],[24,46],[9,6],[30,13],[10,16],[43,10],[32,31],[46,20],[26,10],[41,20],[21,33],[28,40],[42,47],[0,29],[17,0],[17,25],[24,18],[39,15],[37,11],[2,41],[34,44],[2,22],[22,29],[20,8],[43,26],[43,1],[17,22],[9,4],[30,5],[4,7],[10,13],[0,37],[6,8],[23,7],[31,34],[30,39],[41,45],[0,14],[31,29],[3,20],[29,27],[40,42],[35,17],[36,8],[43,8],[2,43],[18,13],[9,44],[34,23],[36,40],[30,2],[7,20],[45,20],[35,40],[38,9],[10,2],[10,40]]))
    # 23
    print(Solution().minimumTotalPrice(n=4, edges=[[0, 1], [1, 2], [1, 3]], price=[2, 2, 10, 6], trips=[[0, 3], [2, 1], [2, 3]]))
    # 1
    print(Solution().minimumTotalPrice(2, edges=[[0, 1]], price=[2, 2], trips=[[0, 0]]))
