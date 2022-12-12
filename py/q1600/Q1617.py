"""
 * 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
 * 一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
 * 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
 * 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
 * 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
 * 提示：
 * 1、2 <= n <= 15
 * 2、edges.length == n-1
 * 3、edges[i].length == 2
 * 4、1 <= ui, vi <= n
 * 5、题目保证 (ui, vi) 所表示的边互不相同。
 * 链接：https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/
"""
from typing import List


class Solution:

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:

        g = [[] for _ in range(n)]  # 图
        paths = [[[] for __ in range(n)] for _ in range(n)]  # 路径
        dis = [[n] * n for _ in range(n)]  # 距离
        for s, e in edges:
            g[s - 1].append(e - 1)
            g[e - 1].append(s - 1)

        def dfs(s, idx, path, v):
            paths[s][idx] = path
            dis[s][idx] = v
            for nx in g[idx]:
                if path and nx == path[-1]: continue
                dfs(s, nx, path[:] + [idx], v + 1)
            return

        for s in range(n):
            dfs(s, s, [], 0)

        ans = [0] * (n - 1)  # 下标从 1 开始
        for m in range(1, 1 << (n)):  # 遍历边集
            arr = []
            for j in range(n + 1):
                if (1 << j) & m: arr.append(j)
            mx, ps = 0, set(arr)
            for x in range(len(arr)):
                for y in range(x + 1, len(arr)):
                    ps.update(paths[arr[x]][arr[y]])  # 统计路径
                    mx = max(mx, dis[arr[x]][arr[y]])
            if mx and len(ps) == m.bit_count():  # 验证路径合法性
                ans[mx - 1] += 1
        return ans


if __name__ == '__main__':
    # [2,1]
    print(Solution().countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]))
    # [1]
    print(Solution().countSubgraphsForEachDiameter(2, [[1, 2]]))
    # [3,4,0]
    print(Solution().countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]))
