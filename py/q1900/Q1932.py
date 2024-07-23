"""
 * 给你 n 个 二叉搜索树的根节点 ，存储在数组 trees 中（下标从 0 开始），对应 n 棵不同的二叉搜索树。
 * trees 中的每棵二叉搜索树 最多有 3 个节点 ，且不存在值相同的两个根节点。
 * 在一步操作中，将会完成下述步骤：
 * 1、选择两个 不同的 下标 i 和 j ，要求满足在 trees[i] 中的某个 叶节点 的值等于 trees[j] 的 根节点的值 。
 * 2、用 trees[j] 替换 trees[i] 中的那个叶节点。
 * 3、从 trees 中移除 trees[j] 。
 * 如果在执行 n - 1 次操作后，能形成一棵有效的二叉搜索树，则返回结果二叉树的 根节点 ；如果无法构造一棵有效的二叉搜索树，返回 null 。
 * 二叉搜索树是一种二叉树，且树中每个节点均满足下述属性：
 * 1、任意节点的左子树中的值都 严格小于 此节点的值。
 * 2、任意节点的右子树中的值都 严格大于 此节点的值。
 * 叶节点是不含子节点的节点。
 * 提示：
 * 1、n == trees.length
 * 2、1 <= n <= 5 * 10^4
 * 3、每棵树中节点数目在范围 [1, 3] 内。
 * 4、输入数据的每个节点可能有子节点但不存在子节点的子节点
 * 5、trees 中不存在两棵树根节点值相同的情况。
 * 6、输入中的所有树都是 有效的二叉树搜索树 。
 * 7、1 <= TreeNode.val <= 5 * 10^4.
 * 链接：https://leetcode.cn/problems/merge-bsts-to-create-single-bst/
"""

from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1932 lang=python3
#
# [1932] 合并多棵二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def canMerge(self, trees: List[TreeNode | None]) -> Optional[TreeNode]:
        d = {}
        for t in trees:
            if not t: continue
            d[t.val] = t
            t.f_l, t.f_r = None, None  # type: ignore
            t.s_l, t.s_r = t, t  # type: ignore
            if t.left:
                t.s_l = t.left  # type: ignore
                t.left.f_l, t.left.f_r = t.left, None
            if t.right:
                t.s_r = t.right  # type: ignore
                t.right.f_l, t.right.f_r = None, t.right

        def dfs(node, dir, fa):
            if not node: return True
            if node.val in d and d[node.val] != node:
                nn = d[node.val]
                if dir == 0:
                    if nn.s_r.val >= fa.val or (fa.f_l and nn.s_l.val <= fa.f_l.val):
                        return False
                    fa.left = nn
                    fa.s_l = nn.s_l
                    nn.f_r = fa
                else:
                    if nn.s_l.val <= fa.val or (fa.f_r and nn.s_r.val >= fa.f_r.val):
                        return False
                    fa.right = nn
                    fa.s_r = nn.s_r
                    nn.f_l = fa
                del d[node.val]
            return dfs(node.left, 0, node) and dfs(node.right, 1, node)

        q = Deque(trees)
        while len(d) > 1:
            n_q, d_size = [], len(d)
            for t in q:
                if not t: continue
                if not t.val in d: continue
                head = TreeNode()
                head.left = t
                # head.l, head.r = 0, 0x3c3c3c3c3c3c  # type: ignore
                v = dfs(t, 0, head)
                if not v: return None
                if head.left:
                    n_q.append(head.left)
            if len(n_q) == 0 or len(d) == d_size:
                return None
            q = n_q
        return list(d.values())[0]


# @lc code=end

if __name__ == '__main__':
    # [1,null,3,2]
    print(Solution().canMerge([stringToTreeNode('[3,2]'), stringToTreeNode('[1,null,3]')]))
    # []
    print(Solution().canMerge(
        [stringToTreeNode('[2,null,5]'),
         stringToTreeNode('[3,1,4]'),
         stringToTreeNode('[1,null,2]')]))
    # []
    print(Solution().canMerge(
        [stringToTreeNode('[1,null,2]'),
         stringToTreeNode('[3,1]'),
         stringToTreeNode('[2,null,3]')]))
    # [3,2,5,1,null,4]
    print(Solution().canMerge([stringToTreeNode('[2,1]'), stringToTreeNode('[3,2,5]'), stringToTreeNode('[5,4]')]))
    # []
    print(Solution().canMerge([stringToTreeNode('[5,4]'), stringToTreeNode('[3]')]))
    # []
    print(Solution().canMerge([stringToTreeNode('[5,3,8]'), stringToTreeNode('[3,2,6]')]))
