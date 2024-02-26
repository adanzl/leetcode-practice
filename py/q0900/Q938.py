"""
 * 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
 * 提示：
 * 1、树中节点数目在范围 [1, 2 * 10^4] 内
 * 2、1 <= Node.val <= 10^5
 * 3、1 <= low <= high <= 10^5
 * 4、所有 Node.val 互不相同
 * 链接：https://leetcode.cn/problems/range-sum-of-bst
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# @lc code=end

if __name__ == '__main__':
    # 32
    print(Solution().rangeSumBST(stringToTreeNode('[10,5,15,3,7,null,18]'), 7, high=15))
    # 23
    print(Solution().rangeSumBST(stringToTreeNode('[10,5,15,3,7,13,18,1,null,6]'), 6, 10))
