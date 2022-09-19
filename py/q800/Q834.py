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

from collections import defaultdict, deque
from typing import *


class Solution:

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        next_map = [list() for _ in range(n)]
        for edge in edges:
            next_map[edge[0]].append(edge[1])
            next_map[edge[1]].append(edge[0])
        subs = [0] * n

        def func(parent, node, subs):
            sub, val = 0, 0
            next_list = next_map[node]
            for next in next_list:
                if next == parent: continue
                s, v = func(node, next, subs)
                sub += s + 1
                val += v
            subs[node] = sub
            return sub, val + sub

        ans[0] = func(-1, 0, subs)[1]
        q = deque()
        for next in next_map[0]:
            q.append((next, ans[0], 0))  # idx-val-parent
        while q:
            idx, val, parent = q.popleft()
            next_list = next_map[idx]
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
