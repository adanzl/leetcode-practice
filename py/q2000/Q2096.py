"""
 * 给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。
 * 每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，
 * 表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。
 * 请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。
 * 每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向：
 * 1、'L' 表示从一个节点前往它的 左孩子 节点。
 * 2、'R' 表示从一个节点前往它的 右孩子 节点。
 * 3、'U' 表示从一个节点前往它的 父 节点。
 * 请你返回从 s 到 t 最短路径 每一步的方向。
 * 提示：
 * 1、树中节点数目为 n 。
 * 2、2 <= n <= 10^5
 * 3、1 <= Node.val <= n
 * 4、树中所有节点的值 互不相同 。
 * 5、1 <= startValue, destValue <= n
 * 6、startValue != destValue
 * 链接：https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
"""

from functools import cache
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=2096 lang=python3
#
# [2096] 从二叉树一个节点到另一个节点每一步的方向
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        s_path, d_path, center = -1, -1, None

        @cache
        def dfs(root):  # start-dest
            nonlocal s_path, d_path, center
            if root == None: return -1, -1
            ret_s, ret_d = -1, -1
            if root.val == startValue:
                ret_s = 0
            if root.val == destValue:
                ret_d = 0
            l_sub, r_sub = dfs(root.left), dfs(root.right)
            if l_sub[0] >= 0:
                ret_s = l_sub[0] + 1
            if l_sub[1] >= 0:
                ret_d = l_sub[1] + 1
            if r_sub[0] >= 0:
                ret_s = r_sub[0] + 1
            if r_sub[1] >= 0:
                ret_d = r_sub[1] + 1

            if ret_s >= 0 and ret_d >= 0 and (s_path < 0 or d_path < 0 or s_path + d_path > ret_s + ret_d):
                s_path, d_path, center = ret_s, ret_d, root

            return ret_s, ret_d

        dfs(root)

        def path(node, d):
            if node is None: return ''
            if node.val == destValue:
                return d
            ret = path(node.left, 'L')
            if ret: return d + ret
            ret = path(node.right, 'R')
            if ret: return d + ret
            return ''

        return 'U' * s_path + path(center, '')


# @lc code=end

if __name__ == '__main__':
    # 'UURR'
    print(Solution().getDirections(stringToTreeNode('[5,8,3,1,null,4,7,6,null,null,null,null,null,null,2]'), 4, 3))
    #
    print(Solution().getDirections(
        stringToTreeNode('[1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]'), 6, 15))
    # "U"
    print(Solution().getDirections(stringToTreeNode('[1,2]'), 2, 1))
    # "UURL"
    print(Solution().getDirections(stringToTreeNode('[5,1,2,3,null,6,4]'), 3, 6))
    # "L"
    print(Solution().getDirections(stringToTreeNode('[2,1]'), 2, 1))
