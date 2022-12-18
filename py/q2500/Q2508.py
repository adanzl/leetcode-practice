"""
 * 给你一个有 n 个节点的 无向 图，节点编号为 1 到 n 。再给你整数 n 和一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条边。图不一定连通。
 * 你可以给图中添加 至多 两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。
 * 如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回 true ，否则返回 false 。
 * 点的度数是连接一个点的边的数目。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、2 <= edges.length <= 10^5
 * 3、edges[i].length == 2
 * 4、1 <= ai, bi <= n
 * 5、ai != bi
 * 6、图中不会有重边
 * 链接：https://leetcode.cn/problems/add-edges-to-make-degrees-of-all-nodes-even/
"""
from typing import List


class Solution:

    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = [set() for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            degree[u] += 1
            degree[v] += 1
        odds = []
        for i in range(1, n + 1):
            if degree[i] % 2 != 0:
                odds.append(i)
        if len(odds) == 0:
            return True
        if len(odds) == 2:
            a, b = odds[0], odds[1]
            if b not in g[a]:
                return True
            for i in range(1, n + 1):
                if i not in [a, b] and i not in g[a] and i not in g[b]:
                    return True
            return False
        if len(odds) == 4:
            a, b, c, d = odds[0], odds[1], odds[2], odds[3]
            if b not in g[a] and c not in g[d]:
                return True
            if c not in g[a] and d not in g[b]:
                return True
            if d not in g[a] and c not in g[b]:
                return True
            return False
        return False


if __name__ == '__main__':
    # False
    print(Solution().isPossible(4, [[1, 2], [1, 3], [1, 4]]))
    # True
    print(Solution().isPossible(5, [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]))
    # True
    print(Solution().isPossible(4, [[1, 2], [3, 4]]))
