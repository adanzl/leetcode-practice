"""
 * 给你一棵二叉树的根节点 root 和一个正整数 k 。
 * 树中的 层和 是指 同一层 上节点值的总和。
 * 返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。
 * 注意，如果两个节点与根节点的距离相同，则认为它们在同一层。
 * 提示：
 * 树中的节点数为 n
 * 1、2 <= n <= 10^5
 * 2、1 <= Node.val <= 10^6
 * 3、1 <= k <= n
 * 链接：https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *
from typing import Optional


class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
        q = [root]
        arr = []
        while q:
            sm = 0
            t = q
            q = []
            for p in t:
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
                sm += p.val
            arr.append(sm)
        if len(arr) < k:
            return -1
        arr.sort()
        return arr[-k]


if __name__ == '__main__':
    # 13
    print(Solution().kthLargestLevelSum(stringToTreeNode("[5,8,9,2,1,3,7,4,6]"), k=2))
    # 3
    print(Solution().kthLargestLevelSum(stringToTreeNode("[1,2,null,3]"), k=1))
