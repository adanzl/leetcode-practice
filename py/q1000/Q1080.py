"""
 * 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
 * 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
 * 叶子节点，就是没有子节点的节点。
 * 提示：
 * 1、树中节点数目在范围 [1, 5000] 内
 * 2、-10^5 <= Node.val <= 10^5
 * 3、-10^9 <= limit <= 10^9
 * 链接：https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode], s: int) -> bool:
            if not node: return False
            if not node.left and not node.right:
                return s + node.val >= limit
            l = dfs(node.left, s + node.val)
            if not l: node.left = None
            r = dfs(node.right, s + node.val)
            if not r: node.right = None
            return l or r

        return root if dfs(root, 0) else None


if __name__ == '__main__':
    # []
    print(Solution().sufficientSubset(stringToTreeNode('[10,5,10]'), 21))
    # [1,2,3,4,null,null,7,8,9,null,14]
    print(Solution().sufficientSubset(stringToTreeNode('[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]'), 1))
    # [5,4,8,11,null,17,4,7,null,null,null,5]
    print(Solution().sufficientSubset(stringToTreeNode('[5,4,8,11,null,17,4,7,1,null,null,5,3]'), 22))
    # [1,null,-3,4]
    print(Solution().sufficientSubset(stringToTreeNode('[1,2,-3,-5,null,4,null]'), -1))
