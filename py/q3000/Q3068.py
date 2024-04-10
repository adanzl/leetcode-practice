"""
 * 给你一棵 n 个节点的 无向 树，节点从 0 到 n - 1 编号。
 * 树以长度为 n - 1 下标从 0 开始的二维整数数组 edges 的形式给你，其中 edges[i] = [ui, vi] 表示树中节点 ui 和 vi 之间有一条边。
 * 同时给你一个 正 整数 k 和一个长度为 n 下标从 0 开始的 非负 整数数组 nums ，其中 nums[i] 表示节点 i 的 价值 。
 * 日增哥哥想 最大化 树中所有节点价值之和。为了实现这一目标，日增哥哥可以执行以下操作 任意 次（包括 0 次）：
 * 选择连接节点 u 和 v 的边 [u, v] ，并将它们的值更新为：
 * 1、nums[u] = nums[u] XOR k
 * 2、nums[v] = nums[v] XOR k
 * 请你返回日增哥哥通过执行以上操作 任意次 后，可以得到所有节点 价值之和 的 最大值 。
 * 提示：
 * 1、2 <= n == nums.length <= 2 * 10^4
 * 2、1 <= k <= 10^9
 * 3、0 <= nums[i] <= 10^9
 * 4、edges.length == n - 1
 * 5、edges[i].length == 2
 * 6、0 <= edges[i][0], edges[i][1] <= n - 1
 * 7、输入保证 edges 构成一棵合法的树。
 * 链接：https://leetcode.cn/problems/find-the-maximum-sum-of-node-values/
"""
from functools import cache
from typing import List


class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def dfs(root, fa, b_xor):
            val = (nums[root] ^ k) if b_xor else nums[root]
            sub = []
            for nx in g[root]:
                if nx == fa: continue
                sub.append([dfs(nx, root, True), dfs(nx, root, False)])
            sub.sort(key=lambda x: x[1] - x[0])
            sm = 0
            for _, f in sub:
                sm += f
            ret = val + sm
            for vv in sub:
                val ^= k
                sm = sm + vv[0] - vv[1]
                ret = max(ret, val + sm)

            return ret

        return dfs(0, -1, False)


if __name__ == '__main__':
    # 9
    print(Solution().maximumValueSum([2, 3], k=7, edges=[[0, 1]]))
    # 6
    print(Solution().maximumValueSum([1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))
    # 42
    print(Solution().maximumValueSum([7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
