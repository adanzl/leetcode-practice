"""
 * 给你一棵 二叉树 的根节点 root 和一个整数k。
 * 返回第 k 大的 完美二叉 子树 的大小，如果不存在则返回 -1。
 * 完美二叉树 是指所有叶子节点都在同一层级的树，且每个父节点恰有两个子节点。
 * 子树 是指树中的某一个节点及其所有后代形成的树。
 * 提示：
 * 1、树中的节点数目在 [1, 2000] 范围内。
 * 2、1 <= Node.val <= 2000
 * 3、1 <= k <= 1024 
 * 链接：https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
"""
from typing import Counter
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

INF = 0x3c3c3c3c3c3c3c3c3c


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        cnt = Counter()

        def dfs(node):
            if node is None:
                return 0
            ld, rd = dfs(node.left), dfs(node.right)
            if ld == rd and ld != -1:
                cnt[ld + rd + 1] += 1
                return ld + rd + 1
            else:
                return -1

        dfs(root)
        tot = 0
        for v in sorted(cnt.keys(), reverse=True):
            tot += cnt[v]
            if tot >= k:
                return v
        return -1


if __name__ == '__main__':
    # 1
    print(Solution().kthLargestPerfectSubtree(stringToTreeNode('[11,11,10,7,2,11]'), 4))
    # 3
    print(Solution().kthLargestPerfectSubtree(stringToTreeNode('[5,3,6,5,2,5,7,1,8,null,null,6,8]'), 2))
    # 7
    print(Solution().kthLargestPerfectSubtree(stringToTreeNode('[1,2,3,4,5,6,7]'), 1))
    # -1
    print(Solution().kthLargestPerfectSubtree(stringToTreeNode('[1,2,3,null,4]'), 3))
