"""
 * 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
 * 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
 * 提示：
 * 1、二叉树中节点数目范围是 [1, 10^5] 。
 * 2、每个节点权值的范围是 [-10^4, 10^4] 。
 * 链接：https://leetcode.cn/problems/count-good-nodes-in-binary-tree/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, v):
            if not node: return
            nonlocal ans
            if node.val >= v:
                ans += 1
            dfs(node.left, max(v, node.val))
            dfs(node.right, max(v, node.val))

        dfs(root, -10**4)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().goodNodes(stringToTreeNode('[3,1,4,3,null,1,5]')))
    # 3
    print(Solution().goodNodes(stringToTreeNode('[3,3,null,4,2]')))
    # 1
    print(Solution().goodNodes(stringToTreeNode('[1]')))