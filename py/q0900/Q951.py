"""
 * 我们可以为二叉树 T 定义一个 翻转操作 ，如下所示：选择任意节点，然后交换它的左子树和右子树。
 * 只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转 等价 于二叉树 Y。
 * 这些树由根节点 root1 和 root2 给出。如果两个二叉树是否是翻转 等价 的函数，则返回 true ，否则返回 false 。
 * 提示：
 * 1、每棵树节点数在 [0, 100] 范围内
 * 2、每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数
 * 链接：https://leetcode.cn/problems/flip-equivalent-binary-trees
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=951 lang=python3
# @lcpr version=20002
#
# [951] 翻转等价二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(r1, r2):
            if r1 is None and r2 is None:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return (dfs(r1.left, r2.left) and dfs(r1.right, r2.right)) or (dfs(r1.left, r2.right) and dfs(r1.right, r2.left))
        return dfs(root1, root2)


# @lc code=end

#

if __name__ == '__main__':
    # True
    print(Solution().flipEquiv(stringToTreeNode('[1,2,3,4,5,6,null,null,null,7,8]'),
                               stringToTreeNode('[1,3,2,null,6,4,5,null,null,null,null,8,7]')))
    # True
    print(Solution().flipEquiv(stringToTreeNode('[]'), stringToTreeNode('[]')))
    # False
    print(Solution().flipEquiv(stringToTreeNode('[]'), stringToTreeNode('[1]')))
