"""
 * 给你二叉树的根节点 root 和一个整数 distance 。
 * 如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
 * 返回树中 好叶子节点对的数量 。
 * 提示：
 * 1、tree 的节点数在 [1, 2^10] 范围内。
 * 2、每个节点的值都在 [1, 100] 之间。
 * 3、1 <= distance <= 10
 * 链接：https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs
"""

from typing import Counter
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=1530 lang=python3
#
# [1530] 好叶子节点对的数量
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countPairs(self, root: TreeNode | None, distance: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            ret = Counter()
            if node is None: return ret
            if node.left is None and node.right is None:
                ret[0] += 1
                return ret
            sub_l = dfs(node.left)
            sub_r = dfs(node.right)
            for l_v in sub_l:
                for r_v in range(distance - 1 - l_v):
                    if r_v in sub_r:
                        ans += sub_l[l_v] * sub_r[r_v]
            for v, c in sub_l.items():
                if v + 1 <= distance:
                    ret[v + 1] += c
            for v, c in sub_r.items():
                if v + 1 <= distance:
                    ret[v + 1] += c
            return ret

        dfs(root)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().countPairs(stringToTreeNode('[1,2,3,null,4]'), 3))
    # 2
    print(Solution().countPairs(stringToTreeNode('[1,2,3,4,5,6,7]'), 3))
    # 1
    print(Solution().countPairs(stringToTreeNode('[7,1,4,6,null,5,3,null,null,null,null,null,2]'), 3))
    # 0
    print(Solution().countPairs(stringToTreeNode('[100]'), 1))
    # 1
    print(Solution().countPairs(stringToTreeNode('[1,1,1]'), 2))
