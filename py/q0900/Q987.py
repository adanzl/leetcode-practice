"""
 * 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
 * 对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。
 * 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。
 * 如果同行同列上有多个结点，则按结点的值从小到大进行排序。
 * 返回二叉树的 垂序遍历 序列。
 * 提示：
 * 1、树中结点数目总数在范围 [1, 1000] 内
 * 2、0 <= Node.val <= 1000
 * 链接：https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/
"""

from collections import defaultdict
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        q = [[root, 0]]
        while q:
            t = []
            line = defaultdict(list)
            for node, col in q:
                line[col].append(node.val)
                if node.left: t.append([node.left, col - 1])
                if node.right: t.append([node.right, col + 1])
            for k, v in line.items():
                dic[k] += sorted(v)
            q = t

        return [dic[k] for k in sorted(dic.keys())]


# @lc code=end

if __name__ == '__main__':
    # [[0],[1],[3,2,2],[4]]
    print(Solution().verticalTraversal(stringToTreeNode('[3,1,4,0,2,2]')))
    # [[9],[3,15],[20],[7]]
    print(Solution().verticalTraversal(stringToTreeNode('[3,9,20,null,null,15,7]')))
    # [[4],[2],[1,5,6],[3],[7]]
    print(Solution().verticalTraversal(stringToTreeNode('[1,2,3,4,5,6,7]')))
    # [[4],[2],[1,5,6],[3],[7]]
    print(Solution().verticalTraversal(stringToTreeNode('[1,2,3,4,6,5,7]')))