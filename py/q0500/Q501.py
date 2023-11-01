"""
 * 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
 * 如果树中有不止一个众数，可以按 任意顺序 返回。
 * 假定 BST 满足如下定义：
 * 1、结点左子树中所含节点的值 小于等于 当前节点的值
 * 2、结点右子树中所含节点的值 大于等于 当前节点的值
 * 3、左子树和右子树都是二叉搜索树
 * 提示：
 * 树中节点的数目在范围 [1, 10^4] 内
 * -10^5 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/find-mode-in-binary-search-tree
"""

from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans_l, ans_v, lst_v, lst_l = 0, [], 10**10, 0
        if root is None: return []
        st = []
        cur = root
        while st or cur:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                if cur.val == lst_v:
                    lst_l += 1
                else:
                    lst_l = 1
                    lst_v = cur.val
                if lst_l > ans_l:
                    ans_l = lst_l
                    ans_v = [lst_v]
                elif lst_l == ans_l:
                    ans_v.append(lst_v)
                cur = cur.right
        return ans_v


# @lc code=end

if __name__ == '__main__':
    # [2,6]
    print(Solution().findMode(stringToTreeNode('[6,2,8,0,4,7,9,null,null,2,6]')))
    # [2]
    print(Solution().findMode(stringToTreeNode('[1,null,2,2]')))
    # [0]
    print(Solution().findMode(stringToTreeNode('[0]')))