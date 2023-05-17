"""
 * 给你一个整数 n 表示一棵 满二叉树 里面节点的数目，节点编号从 1 到 n 。根节点编号为 1 ，树中每个非叶子节点 i 都有两个孩子，分别是左孩子 2 * i 和右孩子 2 * i + 1 。
 * 树中每个节点都有一个值，用下标从 0 开始、长度为 n 的整数数组 cost 表示，其中 cost[i] 是第 i + 1 个节点的值。
 * 每次操作，你可以将树中 任意 节点的值 增加 1 。你可以执行操作 任意 次。
 * 你的目标是让根到每一个 叶子结点 的路径值相等。请你返回 最少 需要执行增加操作多少次。
 * 注意：
 * 满二叉树 指的是一棵树，它满足树中除了叶子节点外每个节点都恰好有 2 个节点，且所有叶子节点距离根节点距离相同。
 * 路径值 指的是路径上所有节点的值之和。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、n + 1 是 2 的幂
 * 3、cost.length == n
 * 4、1 <= cost[i] <= 10^4
 * 链接：https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/
"""
from typing import List


class Solution:

    def minIncrements(self, n: int, cost: List[int]) -> int:
        arr = [0] * ((n + 1) // 2)
        off = (n + 1) // 2
        for i, v in enumerate(arr, start=off):
            ii = i
            while ii:
                arr[i - off] += cost[ii - 1]
                ii >>= 1
        ans = 0
        mx = max(arr)
        for i, v in enumerate(arr):
            arr[i] = mx - v
        while len(arr) > 1:
            t = []
            for i in range(0, len(arr), 2):
                v1, v2 = arr[i], arr[i + 1]
                t.append(min(v1, v2))
                ans += max(v1, v2) - min(v1, v2)
            arr = t
        return ans + arr[0] if arr else 0


if __name__ == '__main__':
    # 15735
    print(Solution().minIncrements(15, cost=[764, 1460, 2664, 764, 2725, 4556, 5305, 8829, 5064, 5929, 7660, 6321, 4830, 7055, 3761]))
    # 6
    print(Solution().minIncrements(7, cost=[1, 5, 2, 2, 3, 3, 1]))
    # 0
    print(Solution().minIncrements(3, cost=[5, 3, 3]))
