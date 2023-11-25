"""
 * 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
 * 提示：
 * 1、给定二叉树的节点数目在范围 [1, 10^5] 内
 * 2、1 <= Node.val <= 9
 * 3、请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
 * 链接：https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree
"""

from collections import Counter
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, cnt):
            if node is None: return
            nonlocal ans
            cnt[node.val] += 1
            if node.left is None and node.right is None and sum([v & 1 for v in cnt.values()]) <= 1:
                ans += 1
            dfs(node.left, cnt)
            dfs(node.right, cnt)
            cnt[node.val] -= 1
        dfs(root, Counter())
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().pseudoPalindromicPaths(stringToTreeNode('[2,3,1,3,1,null,1]')))
    # 1
    print(Solution().pseudoPalindromicPaths(stringToTreeNode('[2,1,1,1,3,null,null,null,null,null,1]')))
    # 1
    print(Solution().pseudoPalindromicPaths(stringToTreeNode('[9]')))
