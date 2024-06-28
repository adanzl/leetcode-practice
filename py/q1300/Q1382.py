"""
 * 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
 * 如果有多种构造方法，请你返回任意一种。
 * 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
 * 提示：
 * 1、树节点的数目在 [1, 10^4] 范围内。
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/balance-a-binary-search-tree
"""

import os
import sys
from typing import List

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1382 lang=python3
#
# [1382] 将二叉搜索树变平衡
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        arr, s = [], []
        p = root
        while p or s:
            if p:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                arr.append(p.val)
                p = p.right

        def build_tree(l, r):
            if l > r: return None
            mid = (l + r) >> 1
            ret = TreeNode()
            ret.val = arr[mid]
            ret.left = build_tree(l, mid - 1)
            ret.right = build_tree(mid + 1, r)
            return ret

        return build_tree(0, len(arr) - 1)


# @lc code=end

if __name__ == '__main__':
    # [2,1,3,null,null,null,4]
    print(Solution().balanceBST(stringToTreeNode('[1,null,2,null,3,null,4,null,null]')))
    # [2,1,3]
    print(Solution().balanceBST(stringToTreeNode('[2,1,3]')))
