"""
 * 给你一棵 n 个节点的 无向 树，节点编号为 0 到 n - 1 ，树的根节点在节点 0 处。
 * 同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
 * 给你一个长度为 n 下标从 0 开始的整数数组 cost ，其中 cost[i] 是第 i 个节点的 开销 。
 * 你需要在树中每个节点都放置金币，在节点 i 处的金币数目计算方法如下：
 * 1、如果节点 i 对应的子树中的节点数目小于 3 ，那么放 1 个金币。
 * 2、否则，计算节点 i 对应的子树内 3 个不同节点的开销乘积的 最大值 ，并在节点 i 处放置对应数目的金币。
 *      如果最大乘积是 负数 ，那么放置 0 个金币。
 * 请你返回一个长度为 n 的数组 coin ，coin[i]是节点 i 处的金币数目。
 * 提示：
 * 1、2 <= n <= 2 * 10^4
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、cost.length == n
 * 6、1 <= |cost[i]| <= 10^4
 * 7、edges 一定是一棵合法的树。
 * 链接：https://leetcode.cn/problems/find-number-of-coins-to-place-in-tree-nodes/
"""
from heapq import heappush, heappushpop
from typing import List


class Solution:

    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def push_l(pos_q, neg_q, val):
            if val > 0:
                q, v = pos_q, val
            else:
                q, v = neg_q, -val
            if len(q) > 2:
                heappushpop(q, v)
            else:
                heappush(q, v)

        ans = [0] * n

        def dfs(idx, fa):
            pos_q, neg_q = [], []  # - +
            for nx in g[idx]:
                if nx == fa: continue
                pq, nq = dfs(nx, idx)
                for p_n in pq:
                    push_l(pos_q, neg_q, p_n)
                for n_n in nq:
                    push_l(pos_q, neg_q, -n_n)
            push_l(pos_q, neg_q, cost[idx])
            if len(pos_q) + len(neg_q) < 3:
                ans[idx] = 1
            else:
                vv = 0
                pos_q.sort()
                neg_q.sort()
                # 0 负
                if len(pos_q) == 3:
                    vv = max(vv, pos_q[0] * pos_q[1] * pos_q[2])
                # 2 负
                if len(pos_q) >= 1 and len(neg_q) >= 2:
                    vv = max(vv, neg_q[-1] * neg_q[-2] * pos_q[-1])
                ans[idx] = vv
            return pos_q, neg_q

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    # [0,1,1]
    print(Solution().placedCoins([[0, 1], [0, 2]], [1, 2, -2]))
    # [1000000000000,1,1,1]
    print(Solution().placedCoins([[0, 1], [0, 2], [2, 3]], [10000, -10000, 10000, -10000]))
    # [120,1,1,1,1,1]
    print(Solution().placedCoins([[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], cost=[1, 2, 3, 4, 5, 6]))
    # [280,140,32,1,1,1,1,1,1]
    print(Solution().placedCoins([[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]],
                                 cost=[1, 4, 2, 3, 5, 7, 8, -4, 2]))
    # [0,1,1]
    print(Solution().placedCoins([[0, 1], [0, 2]], cost=[1, 2, -2]))
