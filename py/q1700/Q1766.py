"""
 * 给你一个 n 个节点的树（也就是一个无环连通无向图），节点编号从 0 到 n - 1 ，且恰好有 n - 1 条边，每个节点有一个值。
 * 树的 根节点 为 0 号点。
 * 给你一个整数数组 nums 和一个二维数组 edges 来表示这棵树。
 * nums[i] 表示第 i 个点的值，edges[j] = [u_j, v_j] 表示节点 u_j 和节点 v_j 在树中有一条边。
 * 当 gcd(x, y) == 1 ，我们称两个数 x 和 y 是 互质的 ，其中 gcd(x, y) 是 x 和 y 的 最大公约数 。
 * 从节点 i 到 根 最短路径上的点都是节点 i 的祖先节点。一个节点 不是 它自己的祖先节点。
 * 请你返回一个大小为 n 的数组 ans ，其中 ans[i]是离节点 i 最近的祖先节点且满足 nums[i] 和 nums[ans[i]] 是 互质的 ，
 * 如果不存在这样的祖先节点，ans[i] 为 -1 。
 * 提示：
 * 1、nums.length == n
 * 2、1 <= nums[i] <= 50
 * 3、1 <= n <= 10^5
 * 4、edges.length == n - 1
 * 5、edges[j].length == 2
 * 6、0 <= u_j, v_j < n
 * 7、u_j != v_j
 * 链接：https://leetcode.cn/problems/tree-of-coprimes
"""

from collections import defaultdict
from math import gcd
from typing import List

#
# @lc app=leetcode.cn id=1766 lang=python3
#
# [1766] 互质树
#

# @lc code=start

prime_set = defaultdict(set)
for i in range(1, 51):
    for j in range(1, 51):
        if gcd(i, j) == 1:
            prime_set[i].add(j)

LIMIT = 0x3c3c3c3c3c


class Solution:

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        prime_idx = defaultdict(lambda: [[-1, -1]])
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = [-1] * n

        def dfs(idx, fa, depth):
            ps = prime_set[nums[idx]]
            val, vd = LIMIT, -1
            for pr in ps:
                ii, d = prime_idx[pr][-1]
                if ii == -1: continue
                if d > vd:
                    vd = d
                    val = ii
            if val != LIMIT:
                ans[idx] = val
            prime_idx[nums[idx]].append([idx, depth])
            for nx in g[idx]:
                if nx == fa: continue
                dfs(nx, idx, depth + 1)
            prime_idx[nums[idx]].pop()

        dfs(0, -1, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    # [-1,21,17,43,10,42,7,13,29,44,17,31,39,10,10,29,32,0,40,23,12,39,12,40,25,35,15,38,40,40,17,24,5,1,19,14,17,21,25,24,14,17,40,25,37,17,10]
    print(Solution().getCoprimes([
        9, 16, 30, 23, 33, 35, 9, 47, 39, 46, 16, 38, 5, 49, 21, 44, 17, 1, 6, 37, 49, 15, 23, 46, 38, 9, 27, 3, 24, 1,
        14, 17, 12, 23, 43, 38, 12, 4, 8, 17, 11, 18, 26, 22, 49, 14, 9
    ], [[17, 0], [30, 17], [41, 30], [10, 30], [13, 10], [7, 13], [6, 7], [45, 10], [2, 10], [14, 2],
        [40, 14], [28, 40], [29, 40], [8, 29], [15, 29], [26, 15], [23, 40], [19, 23], [34, 19], [18, 23], [42, 18],
        [5, 42], [32, 5], [16, 32], [35, 14], [25, 35], [43, 25], [3, 43], [36, 25], [38, 36], [27, 38], [24, 36],
        [31, 24], [11, 31], [39, 24], [12, 39], [20, 12], [22, 12], [21, 39], [1, 21], [33, 1], [37, 1], [44, 37],
        [9, 44], [46, 2], [4, 46]]))
    # [-1,0,0,1]
    print(Solution().getCoprimes([2, 3, 3, 2], edges=[[0, 1], [1, 2], [1, 3]]))

    # [-1,0,-1,0,0,0,-1]
    print(Solution().getCoprimes([5, 6, 10, 2, 3, 6, 15], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
