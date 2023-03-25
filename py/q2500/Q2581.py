"""
 * Alice 有一棵 n 个节点的树，节点编号为 0 到 n - 1 。树用一个长度为 n - 1 的二维整数数组 edges 表示，其中 edges[i] = [ai, bi] ，表示树中节点 ai 和 bi 之间有一条边。
 * Alice 想要 Bob 找到这棵树的根。她允许 Bob 对这棵树进行若干次 猜测 。每一次猜测，Bob 做如下事情：
 * 1、选择两个 不相等 的整数 u 和 v ，且树中必须存在边 [u, v] 。
 * 2、Bob 猜测树中 u 是 v 的 父节点 。
 * Bob 的猜测用二维整数数组 guesses 表示，其中 guesses[j] = [uj, vj] 表示 Bob 猜 uj 是 vj 的父节点。
 * Alice 非常懒，她不想逐个回答 Bob 的猜测，只告诉 Bob 这些猜测里面 至少 有 k 个猜测的结果为 true 。
 * 给你二维整数数组 edges ，Bob 的所有猜测和整数 k ，请你返回可能成为树根的 节点数目 。如果没有这样的树，则返回 0。
 * 提示：
 * 1、edges.length == n - 1
 * 2、2 <= n <= 10^5
 * 3、1 <= guesses.length <= 10^5
 * 4、0 <= ai, bi, uj, vj <= n - 1
 * 5、ai != bi
 * 6、uj != vj
 * 7、edges 表示一棵有效的树。
 * 8、guesses[j] 是树中的一条边。
 * 9、0 <= k <= guesses.length
 * 链接：https://leetcode.cn/problems/count-number-of-possible-root-nodes/
"""
from collections import Counter
from typing import Deque, List


class Solution:

    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        correct = 0
        gus = Counter()
        for u, v in guesses:
            gus[(u, v)] += 1
        e = set()
        # bfs
        q = Deque([[0, -1]])
        while q:
            size = len(q)
            while size:
                p, fa = q.popleft()
                for nx in g[p]:
                    if nx == fa: continue
                    if (p, nx) in gus:
                        correct += gus[(p, nx)]
                    e.add((p, nx))
                    q.append([nx, p])
                size -= 1
        ans = 0 if correct < k else 1

        def dfs(start, fa, correct):
            nonlocal ans
            for nx in g[start]:
                if nx == fa: continue
                vc = correct
                if (start, nx) in e:
                    vc -= gus[(start, nx)]
                if (nx, start) in gus:
                    vc += gus[(nx, start)]
                if vc >= k:
                    ans += 1
                e.add((nx, start))
                e.remove((start, nx))
                dfs(nx, start, vc)
                e.remove((nx, start))
                e.add((start, nx))

        dfs(0, -1, correct)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().rootCount([[0, 1], [2, 0], [0, 3], [4, 2], [3, 5], [6, 0], [1, 7], [2, 8], [2, 9], [4, 10], [9, 11], [3, 12], [13, 8], [14, 9], [15, 9], [10, 16]],
                               [[8, 2], [12, 3], [0, 1], [16, 10]], 2))
    # 3
    print(Solution().rootCount([[0, 1], [1, 2], [1, 3], [4, 2]], guesses=[[1, 3], [0, 1], [1, 0], [2, 4]], k=3))
    # 5
    print(Solution().rootCount([[0, 1], [1, 2], [2, 3], [3, 4]], guesses=[[1, 0], [3, 4], [2, 1], [3, 2]], k=1))