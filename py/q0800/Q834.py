"""
 * 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
 * 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
 * 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。
 * 提示:
 * 1、1 <= n <= 3 * 10^4
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 给定的输入保证为有效的树
 * 链接：https://leetcode.cn/problems/sum-of-distances-in-tree/
"""

from collections import deque
from typing import List


class Solution:

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 换根dp例题
        ans = [0] * n
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        size = [1] * n  # 注意这里初始化成 1 了，下面只需要累加儿子的子树大小

        def dfs(x: int, fa: int, depth: int) -> None:
            ans[0] += depth  # depth 为 0 到 x 的距离
            for y in g[x]:  # 遍历 x 的邻居 y
                if y == fa: continue
                # ！！！ 关键替换代码
                dfs(y, x, depth + 1)  # x 是 y 的父节点
                size[x] += size[y]  # 累加 x 的儿子 y 的子树大小

        dfs(0, -1, 0)  # 先dfs求 0 为根的深度

        def re_root(x: int, fa: int) -> None:
            for y in g[x]:  # 遍历 x 的邻居 y
                if y == fa: continue
                # ！！！ 关键替换代码
                ans[y] = ans[x] + n - 2 * size[y]
                re_root(y, x)  # x 是 y 的父节点

        re_root(0, -1)  # 换根

        return ans

    def sumOfDistancesInTree1(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        subs = [0] * n

        def func(parent, node, subs):
            sub, val = 0, 0
            next_list = g[node]
            for next in next_list:
                if next == parent: continue
                s, v = func(node, next, subs)
                sub += s + 1
                val += v
            subs[node] = sub
            return sub, val + sub

        ans[0] = func(-1, 0, subs)[1]
        q = deque()
        for next in g[0]:
            q.append((next, ans[0], 0))  # idx-val-parent
        while q:
            idx, val, parent = q.popleft()
            next_list = g[idx]
            ans[idx] = val + (n - 1 - subs[idx] - 1) - subs[idx]
            for next in next_list:
                if next == parent: continue
                q.append((next, ans[idx], idx))
        return ans


if __name__ == '__main__':
    # [1,1]
    print(Solution().sumOfDistancesInTree(2, [[0, 1]]))
    # [8,12,6,10,10,10]
    print(Solution().sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
    # [0]
    print(Solution().sumOfDistancesInTree(1, []))
