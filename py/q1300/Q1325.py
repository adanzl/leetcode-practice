"""
 * 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。
 * 注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；
 * 如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。
 * 也就是说，你需要重复此过程直到不能继续删除。
 * 提示：
 * 1、1 <= target <= 1000
 * 2、每一棵树最多有 3000 个节点。
 * 3、每一个节点值的范围是 [1, 1000] 。
 * 链接：https://leetcode.cn/problems/delete-leaves-with-a-given-value
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *
from typing import List

#
# @lc app=leetcode.cn id=1325 lang=python3
#
# [1325] 删除给定值的叶子节点
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(r):
            if not r: return None
            r.left = dfs(r.left)
            r.right = dfs(r.right)
            if not r.left and not r.right and r.val == target: return None
            return r

        return dfs(root)


# @lc code=end

if __name__ == '__main__':
    # [1,null,3,null,4]
    print(Solution().removeLeafNodes(stringToTreeNode('[1,2,3,2,null,2,4]'), 2))
    # [1,3,null,null,2]
    print(Solution().removeLeafNodes(stringToTreeNode('[1,3,3,3,2]'), 3))
    # [1]
    print(Solution().removeLeafNodes(stringToTreeNode('[1,2,null,2,null,2]'), 2))
    # []
    print(Solution().removeLeafNodes(stringToTreeNode('[1,1,1]'), 1))
    # [1,2,3]
    print(Solution().removeLeafNodes(stringToTreeNode('[1,2,3]'), 1))
