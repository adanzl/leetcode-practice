"""
 * 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
 * （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
 * 提示：
 * 1、树中的节点数在 2 到 5000 之间。
 * 2、0 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def f(node, mx, mn):
            if node is None: return
            nonlocal ans
            ans = max(ans, mx - node.val, node.val - mn)
            f(node.left, max(mx, node.val), min(mn, node.val))
            f(node.right, max(mx, node.val), min(mn, node.val))
        f(root, root.val, root.val)
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().maxAncestorDiff(stringToTreeNode('[8,3,10,1,6,null,14,null,null,4,7,13]')))
    # 3
    print(Solution().maxAncestorDiff(stringToTreeNode('[1,null,2,null,0,3]')))