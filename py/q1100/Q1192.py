"""
 * 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，连接是无向的。
 * 用  connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。
 * 任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
 * 关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
 * 请你以任意顺序返回该集群内的所有 关键连接 。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、n - 1 <= connections.length <= 10^5
 * 3、0 <= ai, bi <= n - 1
 * 4、ai != bi
 * 5、不存在重复的连接
 * 链接：https://leetcode.cn/problems/critical-connections-in-a-network/
"""

from typing import List

#
# @lc app=leetcode.cn id=1192 lang=python3
#
# [1192] 查找集群内的关键连接
#


# @lc code=start
class Tarjan:
    # 无向图
    def __init__(self, n) -> None:
        self.g = [[] for _ in range(n)]
        self.idx = 0  # 节点 dfs 时间戳
        self.low = [-1] * n  # 回溯最远点
        self.dfn = [-1] * n  # dfs idx
        self.bridge = []  # 割桥
        self.scc = []  # 割点

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def tarjan(self, u, fa):  # dfs遍历
        self.dfn[u] = self.low[u] = self.idx
        self.idx += 1
        child = 0
        for nx in self.g[u]:
            if nx == fa: continue
            if self.dfn[nx] == -1:
                child += 1
                self.tarjan(nx, u)
                self.low[u] = min(self.low[u], self.low[nx])
                # 此处只处理相邻点的关系
                if self.low[nx] >= self.dfn[u] and u != 0:
                    # 割点 u != 0特判启点
                    # 子树如果不通过u，无法访问更前的节点，最多访问到u，所以当前节点u是割点
                    self.scc.append(u)
                if self.low[nx] > self.dfn[u]:
                    # 割边 此处不需要特判
                    # 子树如果不同u-nx边，无法访问到u，所以u-nx是割桥
                    self.bridge.append([u, nx])
            elif self.dfn[nx] < self.dfn[u]:  #  处理回退
                self.low[u] = min(self.low[u], self.dfn[nx])
        if u == 0 and child >= 2:  # 根节点，有两个不同的子树才能被计算为割点
            self.scc.append(u)


class Solution:

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = Tarjan(n)
        for u, v in connections:
            g.add_edge(u, v)
        g.tarjan(0, 0)
        return g.bridge


# @lc code=end

if __name__ == '__main__':
    # []
    print(Solution().criticalConnections(3, connections=[[0, 1], [1, 2], [0, 2]]))
    # [[0,1]]
    print(Solution().criticalConnections(2, connections=[[0, 1]]))
    # [[1,3]]
    print(Solution().criticalConnections(4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))