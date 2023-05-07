"""
 * 给你一个有 n 个节点的 有向带权 图，节点编号为 0 到 n - 1 。
 * 图中的初始边用数组 edges 表示，其中 edges[i] = [from_i, toi, edgeCost_i] 表示从 from_i 到 toi 有一条代价为 edgeCost_i 的边。
 * 请你实现一个 Graph 类：
 * 1、Graph(int n, int[][] edges) 初始化图有 n 个节点，并输入初始边。
 * 2、addEdge(int[] edge) 向边集中添加一条边，其中 edge = [from, to, edgeCost] 。数据保证添加这条边之前对应的两个节点之间没有有向边。
 * 3、int shortestPath(int node1, int node2) 返回从节点 node1 到 node2 的路径 最小 代价。如果路径不存在，返回 -1 。一条路径的代价是路径中所有边代价之和。
 * 提示：
 * 1、1 <= n <= 100
 * 2、0 <= edges.length <= n * (n - 1)
 * 3、edges[i].length == edge.length == 3
 * 4、0 <= from_i, to_i, from, to, node1, node2 <= n - 1
 * 5、1 <= edgeCost_i, edgeCost <= 10^6
 * 6、图中任何时候都不会有重边和自环。
 * 7、调用 addEdge 至多 100 次。
 * 8、调用 shortestPath 至多 100 次。
 * 链接：https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/
"""
from typing import List

INF = 0x3c3c3c3c


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dis = [[0 if i == j else INF for i in range(n)] for j in range(n)]
        for f, t, v in edges:
            self.dis[f][t] = v
        # Floyed
        for k in range(n):  # 遍历中间节点，此处必须放在最外层
            for i in range(n):
                for j in range(n):
                    self.dis[i][j] = min(self.dis[i][j], self.dis[i][k] + self.dis[k][j])

    def addEdge(self, edge: List[int]) -> None:
        f, t, v = edge
        self.dis[f][t] = min(v, self.dis[f][t])
        for k in [f, t]:
            for i in range(self.n):
                for j in range(self.n):
                    self.dis[i][j] = min(self.dis[i][j], self.dis[i][k] + self.dis[k][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        d = self.dis[node1][node2]
        return d if d != INF else -1


if __name__ == '__main__':
    #
    obj = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(obj.shortestPath(3, 2))  # 6
    print(obj.shortestPath(0, 3))  # -1
    obj.addEdge([1, 3, 4])
    print(obj.shortestPath(0, 3))  # 6
