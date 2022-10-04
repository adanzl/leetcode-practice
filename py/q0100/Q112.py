"""
 * 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
 * 说明: 叶子节点是指没有子节点的节点。
 * 提示：
 * 1、树中节点的数目在范围 [0, 5000] 内
 * 2、-1000 <= Node.val <= 1000
 * 3、-1000 <= targetSum <= 1000
 * 链接：https://leetcode-cn.com/problems/path-sum/
"""
from typing import *

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, targetSum):
            if root is None: return False
            if root.left is None and root.right is None:
                return targetSum == root.val
            return dfs(root.left, targetSum - root.val) or dfs(root.right, targetSum - root.val)

        return dfs(root, targetSum)


if __name__ == '__main__':
    # True
    print(Solution().hasPathSum(stringToTreeNode("[-2,null,-3]"), -5))
    # True
    print(Solution().hasPathSum(stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]"), 22))
    # False
    print(Solution().hasPathSum(stringToTreeNode("[1,2,3]"), 5))
    # False
    print(Solution().hasPathSum(stringToTreeNode("[]"), 0))