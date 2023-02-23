"""
 * 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
 * 差值是一个正数，其数值等于两值之差的绝对值。
 * 提示：
 * 1、树中节点的数目范围是 [2, 100]
 * 2、0 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-distance-between-bst-nodes/
"""
from itertools import pairwise

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        ans = 10**5

        def dfs(node: Optional[TreeNode]):
            if node is None: return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        for a, b in pairwise(sorted(arr)):
            ans = min(ans, b - a)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minDiffInBST(stringToTreeNode("[4,2,6,1,3]")))
    # 1
    print(Solution().minDiffInBST(stringToTreeNode("[1,0,48,null,null,12,49]")))