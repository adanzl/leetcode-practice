"""
 * 给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。
 * 如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。
 * 请你返回修改值之后，树的根 root 。
 * 注意，一个节点的深度指的是从树根节点到这个节点经过的边数。
 * 提示：
 * 1、树中节点数目的范围是 [1, 10^5] 。
 * 2、1 <= Node.val <= 10^4
 * 链接：https://leetcode.cn/problems/cousins-in-binary-tree-ii/
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def func(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if not node:
                return
            if parent:
                if not hasattr(parent, 'sub'): parent.sub = 0  # type: ignore
                parent.sub += node.val  # type: ignore
            func(node.left, node)
            func(node.right, node)

        func(root, None)
        q = [[root, None]]
        d = 0
        dd = []
        while q:
            t = q[:]
            q = []
            sm = 0
            for node, parent in t:
                if node.left:
                    q.append([node.left, node])
                if node.right:
                    q.append([node.right, node])
                if hasattr(node, 'sub'):
                    sm += node.sub  # type: ignore
                if d:
                    node.val = dd[d - 1] - parent.sub
                else:
                    node.val = 0
            dd.append(sm)
            d += 1
        return root


if __name__ == '__main__':
    # [0,0,0,7,7,null,11]
    print(Solution().replaceValueInTree(stringToTreeNode("[5,4,9,1,10,null,7]")))
    # [0,0,0]
    print(Solution().replaceValueInTree(stringToTreeNode("[3,1,2]")))