"""
 * 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：
 * 1、二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
 * 2、偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
 * 3、奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
 * 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。
 * 提示：
 * 1、树中节点数在范围 [1, 10^5] 内
 * 2、1 <= Node.val <= 10^6
 * 链接：https://leetcode.cn/problems/even-odd-tree
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        if root is None: return True
        q = Deque([root])
        end = root
        depth = 0
        pre = None
        while q:
            node = q.popleft()
            if depth & 1:  # odd
                if node.val & 1 or (pre and node.val >= pre.val):
                    return False
            else:  # even
                if not node.val & 1 or (pre and node.val <= pre.val):
                    return False
            pre = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node == end:
                depth += 1
                pre = None
                end = q[-1] if q else None

        return True


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isEvenOddTree(stringToTreeNode('[1,10,4,3,null,7,9,12,8,6,null,null,2]')))
    # False
    print(Solution().isEvenOddTree(stringToTreeNode('[5,4,2,3,3,7]')))
    # False
    print(Solution().isEvenOddTree(stringToTreeNode('[5,9,1,3,5,7]')))
    # True
    print(Solution().isEvenOddTree(stringToTreeNode('[1]')))
