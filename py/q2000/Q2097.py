"""
 * 给你一个下标从 0 开始的二维整数数组 pairs ，其中 pairs[i] = [start_i, end_i] 。
 * 如果 pairs 的一个重新排列，满足对每一个下标 i （ 1 <= i < pairs.length ）都有 end_i-1 == start_i ，
 * 那么我们就认为这个重新排列是 pairs 的一个 合法重新排列 。
 * 请你返回 任意一个 pairs 的合法重新排列。
 * 注意：数据保证至少存在一个 pairs 的合法重新排列。
 * 提示：
 * 1、1 <= pairs.length <= 10^5
 * 2、pairs[i].length == 2
 * 3、0 <= start_i, end_i <= 10^9
 * 4、start_i != end_i
 * 5、pairs 中不存在一模一样的数对。
 * 6、至少 存在 一个合法的 pairs 重新排列。
 * 链接：https://leetcode.cn/problems/valid-arrangement-of-pairs/
"""

from collections import defaultdict
from itertools import pairwise
from typing import List

#
# @lc app=leetcode.cn id=2097 lang=python3
#
# [2097] 合法重新排列数对
#


# @lc code=start
class Graph:

    def __init__(self):
        self.g = defaultdict(list)
        self.o_d = defaultdict(int)
        self.i_d = defaultdict(int)
        self.n_edges = 0

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v]
        self.o_d[u] += 1
        self.i_d[v] += 1
        self.n_edges += 1

    # 求欧拉路（欧拉通路或者欧拉回路）
    # 图连通；除两个端点之外其余节点入度与出度相等；1个节点的入度比初度大1，1个节点的入度比出度小1。
    def find_euler_path(self):
        # 判断是否存在满足条件的起点和终点
        start, end = None, None
        for u in self.g:
            if self.o_d[u] - self.i_d[u] == 1:  # 1个节点的出度比如度大1
                if start is not None: return []  # 存在多个终点
                start = u
            elif self.i_d[u] - self.o_d[u] == 1:  # 1个节点的入度比出度大1
                if end is not None: return []  # 存在多个终点
                end = u
            elif self.i_d[u] != self.o_d[u]:
                return []  # 入度和出度不相等，无法找到满足条件的路径
        if start is None or end is None:  # 无起点和终点，是欧拉回路，就随便找个起点即可
            start = list(self.g.keys())[0]
        # 深度优先搜索
        path = []

        def dfs(node):
            while self.o_d[node] > 0:  # 出度大于0就可以继续走
                self.o_d[node] -= 1
                dfs(self.g[node].pop())
            path.append(node)

        dfs(start)
        # 判断是否找到了有效的路径
        if len(path) != self.n_edges + 1:
            return []

        return path[::-1]


class Solution:

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # 欧拉通路的模板题
        g = Graph()
        for idx, (i, o) in enumerate(pairs):
            g.add_edge(i, o)
        return [[u, v] for u, v in pairwise(g.find_euler_path())]


# @lc code=end

if __name__ == '__main__':
    # [[8, 0], [0, 7], [7, 8], [8, 7], [7, 0], [0, 5], [5, 0], [0, 8], [8, 5]]
    print(Solution().validArrangement([[8, 5], [8, 7], [0, 8], [0, 5], [7, 0], [5, 0], [0, 7], [8, 0], [7, 8]]))
    # [[1,3],[3,2],[2,1]]
    print(Solution().validArrangement([[1, 3], [3, 2], [2, 1]]))
    # [[1,2],[2,1],[1,3]]
    print(Solution().validArrangement([[1, 2], [1, 3], [2, 1]]))
    # [[11,9],[9,4],[4,5],[5,1]]
    print(Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]))
    # [[17,18],[18,10],[10,18]]
    print(Solution().validArrangement([[17, 18], [18, 10], [10, 18]]))
