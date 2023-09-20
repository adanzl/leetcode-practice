"""
 * 给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，
 * 其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
 * 再给你一个长度为 n 的数组 coins ，其中 coins[i] 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。
 * 一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：
 * 1、收集距离当前节点距离为 2 以内的所有金币，或者
 * 2、移动到树中一个相邻节点。
 * 你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。
 * 如果你多次经过一条边，每一次经过都会给答案加一。
 * 提示：
 * 1、n == coins.length
 * 2、1 <= n <= 3 * 104
 * 3、0 <= coins[i] <= 1
 * 4、edges.length == n - 1
 * 5、edges[i].length == 2
 * 6、0 <= ai, bi < n
 * 7、ai != bi
 * 8、edges 表示一棵合法的树。
 * 链接：https://leetcode.cn/problems/collect-coins-in-a-tree/
"""

from typing import List

#
# @lc app=leetcode.cn id=2603 lang=python3
#
# [2603] 收集树中金币
#


# @lc code=start
class Solution:

    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [set() for _ in range(n)]
        in_d = [0] * n
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            in_d[v] += 1
            in_d[u] += 1
        # 移除 0 的叶子结点
        q = [v for v in range(n) if in_d[v] == 1 and coins[v] == 0]
        nn = set(range(n))
        while q:
            v = q.pop(0)
            nn.remove(v)
            for nx in g[v]:
                in_d[nx] -= 1
                if in_d[nx] == 1 and coins[nx] == 0: q.append(nx)
                g[nx].remove(v)
        # 由于可以收集距离2以内的节点，移除 2 次叶子节点
        for _ in range(2):
            q = [v for v in nn if in_d[v] == 1]
            for v in q:
                nn.remove(v)
                for nx in g[v]:
                    in_d[nx] -= 1
                    g[nx].remove(v)
        # 由于是颗 树 ，所以此时剩下的节点都必须访问，同时要回到起点，所以所有的边都需要访问两次，答案为边数*2
        return sum([len(g[v]) for v in nn])


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().collectTheCoins([1, 0, 0, 0, 0, 1], edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))
    # 2
    print(Solution().collectTheCoins([0, 0, 0, 1, 1, 0, 0, 1], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]]))