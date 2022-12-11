"""
 * 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
 * 路径和 是路径中各节点值的总和。
 * 给你一个二叉树的根节点 root ，返回其 最大路径和 。
 * 提示：
 * 1、树中节点数目范围是 [1, 3 * 10^4]
 * 2、-1000 <= Node.val <= 1000
 * 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
"""
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = -0x3c3c3c3c

        def f(node):
            if node is None: return 0
            lv, rv = f(node.left), f(node.right)
            nonlocal ans
            ans = max(ans, lv + rv + node.val)
            return max(max(lv, rv, 0) + node.val, 0)

        f(root)
        return ans


if __name__ == '__main__':
    # 16
    print(Solution().maxPathSum(stringToTreeNode("[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]")))
    # 2
    print(Solution().maxPathSum(stringToTreeNode("[2,-1]")))
    # -3
    print(Solution().maxPathSum(stringToTreeNode("[-3]")))
    # 6
    print(Solution().maxPathSum(stringToTreeNode("[1,2,3]")))
    # 42
    print(Solution().maxPathSum(stringToTreeNode("[-10,9,20,null,null,15,7]")))