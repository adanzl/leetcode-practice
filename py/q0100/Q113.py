"""
 * 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
 * 提示：
 * 1、树中节点总数在范围 [0, 5000] 内
 * 2、-1000 <= Node.val <= 1000
 * 3、-1000 <= targetSum <= 1000
 * 叶子节点 是指没有子节点的节点。
 * 链接：https://leetcode.cn/problems/path-sum-ii/
"""

from typing import *

import sys, os

sys.path.append(os.path.dirname(__file__) + "/../")
from LCUtil import *


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(out, root, target):
            if root is None or target < root.val: return
            if target == root.val and root.left is None and root.right is None:
                ans.append(out + [target])
            dfs(out + [root.val], root.left, target - root.val)
            dfs(out + [root.val], root.right, target - root.val)

        dfs([], root, targetSum)
        return ans


if __name__ == '__main__':
    # [[-2,-3]]
    print(Solution().pathSum(stringToTreeNode("[-2,null,-3]"), -5))
    # [[5,4,11,2],[5,8,4,5]]
    print(Solution().pathSum(stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]"), 22))
    # []
    print(Solution().pathSum(stringToTreeNode("[1,2,3]"), 5))
    # []
    print(Solution().pathSum(stringToTreeNode("[1,2]"), 0))