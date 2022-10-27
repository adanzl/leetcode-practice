"""
 * 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：
 * 1、选择二叉树中 任意 节点和一个方向（左或者右）。
 * 2、如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
 * 3、改变前进方向：左变右或者右变左。
 * 4、重复第二步和第三步，直到你在树中无法继续移动。
 * 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。
 * 请你返回给定树中最长 交错路径 的长度。
 * 提示：
 * 1、每棵树最多有 50000 个节点。
 * 2、每个节点的值在 [1, 100] 之间。
 * 链接：https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # 0: left, 1: right
        def f(root, l, parent):
            if root is None: return l
            vl = f(root.left, (l + 1) if parent == 1 else 0, 0)
            vr = f(root.right, (l + 1) if parent == 0 else 0, 1)
            return max(vl, vr)

        return f(root, 0, -1)


if __name__ == '__main__':
    # 3
    print(Solution().longestZigZag(stringToTreeNode("[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]")))
    # 4
    print(Solution().longestZigZag(stringToTreeNode("[1,1,1,null,1,null,null,1,1,null,1]")))
    # 0
    print(Solution().longestZigZag(stringToTreeNode("[1]")))