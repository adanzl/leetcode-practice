"""
 * 给你一个 值互不相同 的二叉树的根节点 root 。
 * 在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。
 * 返回每一层按 严格递增顺序 排序所需的最少操作数目。
 * 节点的 层数 是该节点和根节点之间的路径的边数。
 * 提示：
 * 1、树中节点的数目在范围 [1, 10^5] 。
 * 2、1 <= Node.val <= 10^5
 * 3、树中的所有值 互不相同 。
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
"""
import os
import sys
from bisect import bisect_left
from typing import Deque, Optional

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = Deque([root])

        # 排序的最小交换次数，要求不能有重复数据 置换环
        # 最小交换次数min_swaps = len(A) - lops(循环环的个数)，环内修改次数：环的大小-1
        def min_swaps(nums):
            a = [bisect_left(sorted(nums), num) for num in nums]  # 记录排序后数值应在的正确位置 离散化数据
            lops = 0
            vis = [False] * len(nums)
            for v in a:
                if vis[v]: continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                lops += 1
            return len(nums) - lops

        while q:
            size = len(q)
            arr = []
            while size:
                cur = q.popleft()
                assert cur
                arr.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                size -= 1
            if len(arr) == 0: continue
            ans += min_swaps(arr)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minimumOperations(stringToTreeNode('[1,3,2,7,6,5,4]')))
    # 3
    print(Solution().minimumOperations(stringToTreeNode('[1, 4, 3, 7, 6, 8, 5, null, null, null, null, 9, null, 10]')))
