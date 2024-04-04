"""
 * 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。
 * 其中，克隆树 cloned 是原始树 original 的一个 副本 。
 * 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。
 * 注意：你 不能 对两棵二叉树，以及 target 节点进行更改。只能 返回对克隆树 cloned 中已有的节点的引用。
 * 提示：
 * 1、树中节点的数量范围为 [1, 10^4] 。
 * 2、同一棵树中，没有值相同的节点。
 * 3、target 节点是树 original 中的一个节点，并且不会是 null 。
 * 链接：https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree
"""

import os
import sys

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode | None:
        path = []

        def get_path(root):
            if root == target:
                return True
            if root == None:
                return False
            path.append(0)
            if get_path(root.left):
                return True
            path.pop()
            path.append(1)
            if get_path(root.right):
                return True
            path.pop()
            return False

        get_path(original)
        ans: TreeNode | None = cloned
        for v in path:
            assert ans is not None
            if v == 0:
                ans = ans.left
            else:
                ans = ans.right
        return ans


# @lc code=end

# if __name__ == '__main__':
#     #
#     print(Solution().getTargetCopy(stringToTreeNode(''), stringToTreeNode(''), 3))
