"""
 * 给你一棵无根带权树，树中总共有 n 个节点，分别表示 n 个服务器，服务器从 0 到 n - 1 编号。
 * 同时给你一个数组 edges ，其中 edges[i] = [a_i, b_i, weight_i] 表示节点 ai 和 bi 之间有一条双向边，边的权值为 weight_i 。
 * 再给你一个整数 signalSpeed 。
 * 如果两个服务器 a ，b 和 c 满足以下条件，那么我们称服务器 a 和 b 是通过服务器 c 可连接的 ：
 * 1、a < b ，a != c 且 b != c 。
 * 2、从 c 到 a 的距离是可以被 signalSpeed 整除的。
 * 3、从 c 到 b 的距离是可以被 signalSpeed 整除的。
 * 4、从 c 到 b 的路径与从 c 到 a 的路径没有任何公共边。
 * 请你返回一个长度为 n 的整数数组 count ，其中 count[i] 表示通过服务器 i 可连接 的服务器对的 数目 。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、edges.length == n - 1
 * 3、edges[i].length == 3
 * 4、0 <= a_i, b_i < n
 * 5、edges[i] = [ai, bi, weight_i]
 * 6、1 <= weight_i <= 10^6
 * 7、1 <= signalSpeed <= 10^6
 * 8、输入保证 edges 构成一棵合法的树。
 * 链接：https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
"""
from collections import Counter
from functools import cache
from typing import List


class Solution:

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append([y, w])
            g[y].append([x, w])

        @cache
        def calc(root, fa):
            ret = Counter([0])
            for nx, nv in g[root]:
                if nx == fa: continue
                sub = calc(nx, root)
                for v, c in sub.items():
                    ret[v + nv] += c
            return ret

        ans = [0] * n
        for i in range(n):
            ss = []
            for sub in g[i]:
                s = calc(sub[0], i)
                cnt = sum([c for v, c in s.items() if (v + sub[1]) % signalSpeed == 0])
                ss.append(cnt)
            for j in range(len(ss)):
                for k in range(j + 1, len(ss)):
                    ans[i] += ss[j] * ss[k]
        return ans


if __name__ == '__main__':
    # [0,4,6,6,4,0]
    print(Solution().countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],
                                                    signalSpeed=1))
    # [2,0,0,0,0,0,2]
    print(Solution().countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],
                                                    signalSpeed=3))
