"""
 * 一个 n 个节点的无向树，节点编号为 0 到 n - 1 ，树的根结点是 0 号节点。给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 在树中有一条边。
 * 在每一个节点 i 处有一扇门。同时给你一个都是偶数的数组 amount ，其中 amount[i] 表示：
 * 1、如果 amount[i] 的值是负数，那么它表示打开节点 i 处门扣除的分数。
 * 2、如果 amount[i] 的值是正数，那么它表示打开节点 i 处门加上的分数。
 * 游戏按照如下规则进行：
 * 1、一开始，Alice 在节点 0 处，Bob 在节点 bob 处。
 * 2、每一秒钟，Alice 和 Bob 分别 移动到相邻的节点。Alice 朝着某个 叶子结点 移动，Bob 朝着节点 0 移动。
 * 3、对于他们之间路径上的 每一个 节点，Alice 和 Bob 要么打开门并扣分，要么打开门并加分。注意：
 *   a、如果门 已经打开 （被另一个人打开），不会有额外加分也不会扣分。
 *   b、如果 Alice 和 Bob 同时 到达一个节点，他们会共享这个节点的加分或者扣分。换言之，如果打开这扇门扣 c 分，那么 Alice 和 Bob 分别扣 c / 2 分。如果这扇门的加分为 c ，那么他们分别加 c / 2 分。
 * 4、如果 Alice 到达了一个叶子结点，她会停止移动。类似的，如果 Bob 到达了节点 0 ，他也会停止移动。注意这些事件互相 独立 ，不会影响另一方移动。
 * 请你返回 Alice 朝最优叶子结点移动的 最大 净得分。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 6、edges 表示一棵有效的树。
 * 7、1 <= bob < n
 * 8、amount.length == n
 * 9、amount[i] 是范围 [-10^4, 10^4] 之间的一个 偶数 。
 * 链接：https://leetcode.cn/problems/most-profitable-path-in-a-tree/
"""
from typing import List


class Solution:

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        inf = 0x3c3c3c3c
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for s, e in edges:
            g[s].append(e)
            g[e].append(s)
        bob_time = [n] * n

        def dfs_bob(idx, parent, time):
            if idx == 0:
                bob_time[idx] = time
                return True
            for nx_i in g[idx]:
                if nx_i == parent: continue
                if dfs_bob(nx_i, idx, time + 1):
                    bob_time[idx] = time
                    return True

            return False

        dfs_bob(bob, -1, 0)
        g[0].append(-1)
        ans = -inf

        def dfs_alice(idx, parent, time, score):
            nonlocal ans
            if len(g[idx]) == 1:  # 叶子节点
                ans = max(ans, score)
                return
            for nx_i in g[idx]:
                if nx_i == parent: continue
                n_score = score
                if time + 1 < bob_time[nx_i]:
                    n_score += amount[nx_i]
                elif time + 1 == bob_time[nx_i]:
                    n_score += amount[nx_i] // 2
                dfs_alice(nx_i, idx, time + 1, n_score)

        dfs_alice(0, -1, 0, amount[0])
        return ans


if __name__ == '__main__':
    # -7280
    print(Solution().mostProfitablePath([[0, 1]], 1, [-7280, 2350]))
    # 6
    print(Solution().mostProfitablePath([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]))
