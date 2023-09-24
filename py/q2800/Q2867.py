"""
 * 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，
 * 其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。
 * 请你返回树中的 合法路径数目 。
 * 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。
 * 注意：
 * 1、路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
 * 2、路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、1 <= ui, vi <= n
 * 5、输入保证 edges 形成一棵合法的树。
 * 链接：https://leetcode.cn/problems/count-valid-paths-in-a-tree/
"""
from typing import List

LIMIT = 10**5 + 5
prime_list = []
b_composite = [False] * LIMIT
b_composite[1] = True  # 这里 1 被算为合数


def build_prime_list():
    # 线性筛选质数
    for i in range(2, LIMIT):
        if not b_composite[i]:
            prime_list.append(i)
        for prime in prime_list:
            nx = prime * i
            if nx < LIMIT:
                b_composite[nx] = True
            else:
                break


build_prime_list()


class Solution:

    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)
        ans = 0

        def dfs(node, fa):  # cnt_p0, cnt_p1
            nonlocal ans
            ret = 0
            cnt_p0, cnt_p1 = (1, 0) if b_composite[node + 1] else (0, 1)
            for nx in g[node]:
                if nx == fa: continue
                c0, c1 = dfs(nx, node)
                ret += c0 * cnt_p1
                ret += c1 * cnt_p0
                if b_composite[node + 1]:  # 合数
                    cnt_p0 += c0
                    cnt_p1 += c1
                else:
                    cnt_p1 += c0
            ans += ret
            return cnt_p0, cnt_p1

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().countPaths(6, edges=[[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]))
    # 4
    print(Solution().countPaths(5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]]))