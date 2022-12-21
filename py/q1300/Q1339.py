"""
 * 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。
 * 由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。
 * 提示：
 * 1、每棵树最多有 50000 个节点，且至少有 2 个节点。
 * 2、每个节点的值在 [1, 10000] 之间。
 * 链接：https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/
"""
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        ans = 0

        def f(node):
            if node is None: return 0
            node.sm = f(node.left) + f(node.right) + node.val
            return node.sm

        f(root)

        def walk(node, root):
            if node is None: return
            if root is None: root = node
            nonlocal ans
            if node.left:
                ans = max(ans, node.left.sm * (root.sm - node.left.sm))
            if node.right:
                ans = max(ans, node.right.sm * (root.sm - node.right.sm))
            walk(node.left, root)
            walk(node.right, root)

        walk(root, None)
        return ans % MOD


if __name__ == '__main__':
    # 110
    print(Solution().maxProduct(stringToTreeNode('[1,2,3,4,5,6]')))
    # 90
    print(Solution().maxProduct(stringToTreeNode('[1,null,2,3,4,null,null,5,6]')))
    # 1025
    print(Solution().maxProduct(stringToTreeNode('[2,3,9,10,7,8,6,5,4,11,1]')))
    # 1
    print(Solution().maxProduct(stringToTreeNode('[1,1]')))