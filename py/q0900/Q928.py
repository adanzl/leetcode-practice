"""
 * 给定一个由 n 个节点组成的网络，用 n x n 个邻接矩阵 graph 表示。在节点网络中，只有当 graph[i][j] = 1 时，节点 i 能够直接连接到另一个节点 j。
 * 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。
 * 这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
 * 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
 * 我们可以从 initial 中删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。
 * 请返回移除后能够使 M(initial) 最小化的节点。如果有多个节点满足条件，返回索引 最小的节点 。
 * 注：这个最小的意思是节点的索引，不是在initial中的索引
 * 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后仍有可能因恶意软件传播而受到感染。
 * 提示：
 * 1、n == graph.length
 * 2、n == graph[i].length
 * 3、2 <= n <= 300
 * 4、graph[i][j] == 0 或 1.
 * 5、graph[i][j] == graph[j][i]
 * 6、graph[i][i] == 1
 * 7、1 <= initial.length < n
 * 8、0 <= initial[i] <= n - 1
 * 9、initial 中所有整数均不重复
 * 链接：https://leetcode.cn/problems/minimize-malware-spread-ii/
"""

from typing import List

#
# @lc app=leetcode.cn id=928 lang=python3
#


# @lc code=start
class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)

        def find(parent, x):
            if parent[x] == x: return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def func(skip):
            parent = [i for i in range(n)]
            size = [1] * n

            for i in range(n):
                for j in range(i + 1, n):
                    if i == skip or j == skip: continue
                    if graph[i][j] == 0: continue
                    r0, r1 = find(parent, i), find(parent, j)
                    if r0 != r1:
                        parent[r1] = r0
                        size[r0] += size[r1]
            ans = 0
            for v in initial:
                if v == skip: continue
                r = find(parent, v)
                ans += size[r]
                size[r] = 0
            return ans

        return min([[func(i), i] for i in initial])[1]


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().minMalwareSpread([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]))
    # 1
    print(Solution().minMalwareSpread([[1, 1, 0], [1, 1, 1], [0, 1, 1]], initial=[0, 1]))
    # 3
    print(Solution().minMalwareSpread([[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], [7, 8, 6, 2, 3]))
    # 0
    print(Solution().minMalwareSpread([[1, 1, 0], [1, 1, 0], [0, 0, 1]], initial=[0, 1]))
    # 1
    print(Solution().minMalwareSpread([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]], initial=[0, 1]))
